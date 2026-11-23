"""GEP1316 Ödev 3: bir hedefi yenmek için vuruş ve süre hesabı."""

from math import ceil, isfinite  # Yukarı yuvarlama ve sonlu sayı kontrolü.


def hesapla(hedef_cani, vurus_hasari, vurus_araligi):  # Sayısal girdiler.
    if not 1 <= hedef_cani <= 1000000:  # Can aralığını denetleriz.
        raise ValueError("Hedef canı 1-1000000 arasında olmalı.")
    if not 1 <= vurus_hasari <= 1000000:  # Sıfıra bölmeyi de önleriz.
        raise ValueError("Vuruş hasarı 1-1000000 arasında olmalı.")
    if not isfinite(vurus_araligi) or not 0 < vurus_araligi <= 60:
        raise ValueError("Vuruş aralığı 0'dan büyük, en fazla 60 sn olmalı.")
    vurus_sayisi = ceil(hedef_cani / vurus_hasari)  # Eksik vuruş sayılmaz.
    sure = (vurus_sayisi - 1) * vurus_araligi  # İlk vuruş 0. saniyede.
    dps = vurus_hasari / vurus_araligi  # Saniye başına ortalama hasar.
    tek_vurus = vurus_hasari >= hedef_cani  # Karşılaştırmadan bool oluşur.
    return vurus_sayisi, sure, dps, tek_vurus  # Sonuçları birlikte veririz.


def main():  # Kullanıcıdan bilgileri alan ana fonksiyon.
    try:  # Tür dönüşümü ve sınır hatalarını yakalarız.
        karakter = input("Karakter adı: ").strip()  # str veri tipi.
        if not 2 <= len(karakter) <= 60:  # Kısa ve boş adları denetleriz.
            raise ValueError("Karakter adı 2-60 karakter olmalı.")
        hedef_cani = int(input("Hedef canı: "))  # int dönüşümü.
        vurus_hasari = int(input("Vuruş başına hasar: "))  # int dönüşümü.
        metin = input("Vuruş aralığı (saniye): ").replace(",", ".")
        vurus_araligi = float(metin)  # Ondalıklı girdiyi float yaparız.
        adet, sure, dps, tek_vurus = hesapla(  # Fonksiyonu çağırırız.
            hedef_cani, vurus_hasari, vurus_araligi  # Girdileri aktarırız.
        )  # Fonksiyon çağrısını bitiririz.
        print(f"\n{karakter} için saldırı özeti")  # Başlığı biçimleriz.
        print(f"Gerekli vuruş: {adet}")  # Hesap sonucu bir int değeridir.
        print(f"Hedefi yenme süresi: {sure:.2f} saniye")  # İki ondalık.
        print(f"Saniye başına hasar: {dps:.2f}")  # float biçimlendirme.
        print(f"Tek vuruşta yenilir mi: {'Evet' if tek_vurus else 'Hayır'}")
        print("Varsayım: İlk vuruş 0. saniyede; zırh ve ıskalama yok.")
    except ValueError as hata:  # Hatalı sayı veya değer durumunda...
        print(f"Uyarı: {hata}")  # Anlaşılır bir mesaj gösteririz.
    except (EOFError, KeyboardInterrupt):  # Kullanıcı girişi keserse...
        print("\nİşlem iptal edildi.")  # Programı düzgün sonlandırırız.


if __name__ == "__main__":  # Dosya doğrudan çalıştırılırsa...
    main()  # Kullanıcı arayüzünü başlatırız.
