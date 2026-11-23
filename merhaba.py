"""GEP1316 Ödev 2: ad ve doğum yılıyla karşılama."""

from datetime import date  # Geçerli yılı sistem tarihinden alırız.


def yas_hesapla(dogum_yili, bu_yil):  # Yılları tam sayı olarak alır.
    if dogum_yili > bu_yil:  # Gelecekteki bir doğum yılı geçerli değildir.
        raise ValueError("Doğum yılı gelecekte olamaz.")  # Uyarı üretir.
    if dogum_yili < 1:  # Takvim yılı pozitif olmalıdır.
        raise ValueError("Doğum yılı en az 1 olmalı.")  # Hatayı açıklar.
    return bu_yil - dogum_yili  # Yıl farkını tam sayı olarak döndürür.


def main():  # Kullanıcıyla konuşan ana fonksiyondur.
    bu_yil = date.today().year  # Örneğin 2026; koda sabit yazılmaz.
    try:  # Geçersiz girişleri yakalamak için bu bloğu kullanırız.
        ad = input("Adınız: ").strip()  # Metni alır, kenar boşlukları siler.
        if not 2 <= len(ad) <= 60:  # Ad uzunluğunu kontrol ederiz.
            raise ValueError("Adınızı 2-60 karakter arasında yazın.")
        yil_metni = input("Doğum yılınız: ")  # input sonucu bir metindir.
        dogum_yili = int(yil_metni)  # Metni tam sayıya dönüştürürüz.
        yas = yas_hesapla(dogum_yili, bu_yil)  # Yıl farkını hesaplarız.
        print(f"Merhaba {ad}! Oyun atölyeme hoş geldin.")  # Kişiye özeldir.
        print(f"{bu_yil} yılında {yas} yaşını dolduruyorsun.")  # f-string.
        print("Bu hesap yalnız doğum yılına göre yapılmıştır.")  # Sınırıdır.
    except ValueError as hata:  # Dönüşüm ve doğrulama hatalarını yakalar.
        print(f"Uyarı: {hata}")  # Program iz yığınıyla çökmez.
    except (EOFError, KeyboardInterrupt):  # Girdi biterse veya kesilirse...
        print("\nİşlem iptal edildi.")  # Düzgün bir kapanış mesajı veririz.


if __name__ == "__main__":  # Dosya doğrudan çalıştırıldığında...
    main()  # Ana fonksiyonu başlatırız.
