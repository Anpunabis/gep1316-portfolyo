"""Oyun Atölyesi: standart Python kütüphanesiyle bütçe takibi."""

import csv
import io
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

KLASOR = Path(__file__).resolve().parent
VERI_DOSYASI = KLASOR / "veriler.csv"
ALANLAR = ["tarih", "tur", "aciklama", "tutar"]


def tutar_dogrula(metin):
    """Kuruş hassasiyetinde, pozitif ve sınırlı bir tutar döndürür."""
    metin = metin.strip().replace(",", ".")
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", metin):
        raise ValueError("Tutarı 125 veya 125,50 biçiminde yazın; binlik ayırıcı kullanmayın.")
    try:
        tutar = Decimal(metin)
    except InvalidOperation:
        raise ValueError("Geçerli bir tutar yazın.") from None
    if not Decimal("0") < tutar <= Decimal("1000000"):
        raise ValueError("Tutar 0'dan büyük, en fazla 1.000.000 TL olmalı.")
    return tutar.quantize(Decimal("0.01"))


def tarih_dogrula(metin):
    metin = metin.strip()
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", metin):
        raise ValueError("Tarih YYYY-AA-GG biçiminde olmalı; örnek: 2030-05-10.")
    try:
        datetime.strptime(metin, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Takvimde geçerli bir tarih yazın.") from None
    return metin


def tur_dogrula(metin):
    tur = metin.strip().lower()
    if tur not in ("gelir", "gider"):
        raise ValueError("İşlem türü gelir veya gider olmalı.")
    return tur


def aciklama_dogrula(metin):
    metin = metin.strip()
    if not 2 <= len(metin) <= 60 or any(ord(c) < 32 for c in metin):
        raise ValueError("Açıklama 2-60 karakter olmalı ve kontrol karakteri içermemeli.")
    if metin.startswith(("=", "+", "-", "@")):
        raise ValueError("Açıklama =, +, - veya @ ile başlayamaz (CSV güvenliği).")
    return metin


def girdi_al(soru, dogrulayici):
    """Hatalı girişte aynı soruyu yeniden sorar."""
    while True:
        try:
            return dogrulayici(input(soru))
        except ValueError as hata:
            print(f"Uyarı: {hata}")


def kayitlari_oku(dosya):
    if not dosya.exists():
        return []
    kayitlar = []
    with dosya.open(encoding="utf-8-sig", newline="") as akis:
        okuyucu = csv.DictReader(akis)
        if okuyucu.fieldnames != ALANLAR:
            raise ValueError("Veri dosyasının sütunları beklenen biçimde değil.")
        for satir_no, satir in enumerate(okuyucu, start=2):
            try:
                if set(satir) != set(ALANLAR) or None in satir.values():
                    raise ValueError("Eksik veya fazla sütun var.")
                kayitlar.append({
                    "tarih": tarih_dogrula(satir["tarih"]),
                    "tur": tur_dogrula(satir["tur"]),
                    "aciklama": aciklama_dogrula(satir["aciklama"]),
                    "tutar": tutar_dogrula(satir["tutar"]),
                })
            except ValueError as hata:
                raise ValueError(f"Veri dosyası, satır {satir_no}: {hata}") from None
    return kayitlar


def csv_kaydet(dosya, alanlar, satirlar):
    """Önce geçici dosyaya yazar; başarılı olunca hedefi değiştirir."""
    gecici = dosya.with_suffix(dosya.suffix + ".tmp")
    try:
        with gecici.open("w", encoding="utf-8-sig", newline="") as akis:
            yazici = csv.DictWriter(akis, fieldnames=alanlar)
            yazici.writeheader()
            yazici.writerows(satirlar)
        gecici.replace(dosya)
    finally:
        if gecici.exists():
            gecici.unlink()


def para_yaz(tutar):
    return f"{tutar:.2f}".replace(".", ",") + " TL"


def toplam_hesapla(kayitlar):
    gelir = Decimal("0.00")
    gider = Decimal("0.00")
    for kayit in kayitlar:
        if kayit["tur"] == "gelir":
            gelir += kayit["tutar"]
        else:
            gider += kayit["tutar"]
    return gelir, gider, gelir - gider


def rapor_metni(kayitlar, baslik):
    cikti = io.StringIO()
    print(f"\n{baslik}", file=cikti)
    print("=" * 78, file=cikti)
    print(f"{'Tarih':10} | {'Tür':5} | {'Açıklama':36} | Tutar", file=cikti)
    for k in kayitlar:
        print(f"{k['tarih']} | {k['tur']:5} | {k['aciklama'][:36]:36} | {para_yaz(k['tutar'])}", file=cikti)
    if not kayitlar:
        print("Henüz kayıt yok.", file=cikti)
    gelir, gider, bakiye = toplam_hesapla(kayitlar)
    print("-" * 78, file=cikti)
    print(f"Gelir: {para_yaz(gelir)} | Gider: {para_yaz(gider)}", file=cikti)
    print(f"Bakiye: {para_yaz(bakiye)}", file=cikti)
    if bakiye < 0:
        print("Uyarı: Harcamalar geliri aşıyor; bütçe açığı var.", file=cikti)
    elif bakiye == 0:
        print("Durum: Bütçe dengede.", file=cikti)
    else:
        print("Durum: Kullanılabilir bütçe var.", file=cikti)
    return cikti.getvalue()


def kayit_ekle(kayitlar, dosya):
    kayit = {
        "tarih": girdi_al("Tarih (YYYY-AA-GG): ", tarih_dogrula),
        "tur": girdi_al("İşlem türü (gelir/gider): ", tur_dogrula),
        "aciklama": girdi_al("Açıklama (2-60 karakter): ", aciklama_dogrula),
        "tutar": girdi_al("Tutar (TL): ", tutar_dogrula),
    }
    # Diske yazılamazsa bellekte de kaydedilmiş gibi göstermeyiz.
    yeni_liste = kayitlar + [kayit]
    csv_kaydet(dosya, ALANLAR, yeni_liste)
    kayitlar.append(kayit)
    print("Kayıt kaydedildi.")


def gunluk_rapor(kayitlar, klasor):
    tarih = girdi_al("Rapor tarihi (YYYY-AA-GG): ", tarih_dogrula)
    secilen = [k for k in kayitlar if k["tarih"] == tarih]
    print(rapor_metni(secilen, f"GÜNLÜK RAPOR / {tarih}"))
    gelir, gider, bakiye = toplam_hesapla(secilen)
    dosya = klasor / f"rapor_{tarih}.csv"
    csv_kaydet(dosya, ["tarih", "kayit_sayisi", "gelir", "gider", "bakiye"], [{
        "tarih": tarih, "kayit_sayisi": len(secilen),
        "gelir": gelir, "gider": gider, "bakiye": bakiye,
    }])
    print(f"Rapor kaydedildi: {dosya.name}")


def main(dosya=VERI_DOSYASI):
    try:
        kayitlar = kayitlari_oku(dosya)
    except (OSError, ValueError, UnicodeError, csv.Error) as hata:
        print(f"Veri dosyası okunamadı: {hata}\nMevcut dosya değiştirilmedi.")
        return
    print("OYUN ATÖLYESİ / Oyun Geliştirme Bütçe Takibi")
    while True:
        print("\n1 - Kayıt ekle\n2 - Tüm kayıtlar ve bütçe\n3 - Günlük rapor ve CSV\n0 - Çıkış")
        try:
            secim = input("Seçiminiz: ").strip()
            if secim == "1":
                kayit_ekle(kayitlar, dosya)
            elif secim == "2":
                print(rapor_metni(kayitlar, "TÜM KAYITLAR / BÜTÇE ÖZETİ"))
            elif secim == "3":
                gunluk_rapor(kayitlar, dosya.parent)
            elif secim == "0":
                print("Görüşmek üzere.")
                break
            else:
                print("Uyarı: Menüden 0, 1, 2 veya 3 seçin.")
        except (EOFError, KeyboardInterrupt):
            print("\nİşlem iptal edildi. Önceden kaydedilen kayıtlar korundu.")
            break
        except (OSError, csv.Error) as hata:
            print(f"Dosya kaydedilemedi: {hata}. Yazma iznini ve boş alanı kontrol edin.")


if __name__ == "__main__":
    main()
