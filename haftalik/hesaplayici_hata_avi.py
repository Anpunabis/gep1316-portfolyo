"""Hata avı alıştırması: Bu sürüm kasıtlı bir mantık hatası içerir."""


def hesapla(hedef_cani, vurus_hasari, vurus_araligi):
    if hedef_cani <= 0 or vurus_hasari <= 0 or vurus_araligi <= 0:
        raise ValueError("Girdiler pozitif olmalı.")
    vurus_sayisi = int(hedef_cani / vurus_hasari)
    sure = max(0, vurus_sayisi - 1) * vurus_araligi
    return vurus_sayisi, sure


if __name__ == "__main__":
    try:
        can = int(input("Hedef canı: "))
        hasar = int(input("Vuruş başına hasar: "))
        aralik = float(input("Vuruş aralığı: ").replace(",", "."))
        adet, sure = hesapla(can, hasar, aralik)
        print(f"Gerekli vuruş: {adet}; hedefi yenme süresi: {sure:.2f} sn")
        print("Varsayım: İlk vuruş 0. saniyede; zırh ve ıskalama yok.")
    except (ValueError, EOFError, KeyboardInterrupt) as hata:
        print(f"Uyarı: {hata}")
