# YZ ile çalışma günlüğü

Araç: OpenAI Codex. Tarih: 6 Kasım 2026.

## Gerçek kullanıcı girdileri

- “Tamam, şimdi ikinci ödevi yap.”
- “Anpunabis; ikinci ödevin bilgilerini ilk mesajımda paylaşmıştım.”
- Kişisel yansıtma için: “Kodlama bilgim zaten vardı, o yüzden çok da zor gelmiyordu ama bu ders bana çok şey öğretti.”

## Altı geliştirme istemi - süreç kaydı

Aşağıdaki altı kayıt, ilk kullanıcı talebini yerine getirmek için izlenen alt görevlerin istem biçiminde düzenlenmiş özetidir. Öğrencinin ayrı ayrı gönderdiği altı mesajın dökümü değildir. Yanıtlar yapılan işi, kararlar geliştirici asistanın gerekçelerini anlatır. Öğrenci kendi gerçek istemlerini ve değerlendirmelerini ekleyerek kişisel günlüğünü tamamlamalıdır.

## 1. Site yapısı
**Çalışma istemi:** Jahan Teymurlu için HTML/CSS/JS ile ana sayfa, hakkımda, projeler ve iletişim sayfalarını oluştur.

**YZ yanıtı/uygulama:** Dört ana sayfa ve yedi ayrıntı sayfası hazırlandı.

**Karar ve gerekçe:** Kabul: ortak gezinti ve ortak dosyalar sağlandı.

## 2. Görsel düzen
**Çalışma istemi:** Dijital Oyun Tasarımı alanına uygun, sade ve duyarlı bir portfolyo tasarla.

**YZ yanıtı/uygulama:** Yerel SVG monogram ve şemalar, serif başlıklar, siyah-beyaz palet kullanıldı.

**Karar ve gerekçe:** Düzenleme: stok fotoğraf yerine kimlik uydurmayan JT avatarı seçildi.

## 3. Proje kaynakları
**Çalışma istemi:** Anpunabis profilindeki gerçek projeleri doğrula; yeni demoları eski ödev gibi sunma.

**YZ yanıtı/uygulama:** Üç mevcut GitHub deposu incelendi; üç yeni demo ayrıca etiketlendi.

**Karar ve gerekçe:** Red: doğrulanmayan oyun özellikleri ve GEP1316 ödev numaraları eklenmedi.

## 4. Etkileşim ve gizlilik
**Çalışma istemi:** Tema, menü, filtre/arama ve doğrulamalı iletişim formu ekle; formun davranışını açıkla.

**YZ yanıtı/uygulama:** Form yalnız taslak üretir; veri saklamaz. Kopyalama ve güvenli metin çıktısı eklendi.

**Karar ve gerekçe:** Düzenleme: gönderilmiş mesaj izlenimi verilmedi; textContent ve form-action none kullanıldı.

## 5. Erişilebilirlik düzeltmesi
**Çalışma istemi:** Mobil menüyü klavye ile aç, Tab ve Escape davranışını test et.

**YZ yanıtı/uygulama:** İlk sürümde Tab menü bağlantılarını atladı. Açılışta ilk bağlantıya focus eklendi.

**Karar ve gerekçe:** İlk hali reddet/düzelt: düzeltme sonrası odak gezintiye geçti, Escape düğmeye döndürdü.

## 6. Kanıt ve teslim
**Çalışma istemi:** Üç ekran boyutunu, form hatalarını ve demoları test et; rapor ve yayın dosyalarını hazırla.

**YZ yanıtı/uygulama:** 33 yerleşim ölçümü, gerçek ekran görüntüleri, form testleri ve 3 sayfalık rapor hazırlandı.

**Karar ve gerekçe:** Kabul: teknik kanıtlar dosyalandı. GitHub oturumu olmadığı için yayında denmedi.

## Kanıtlanmış erişilebilirlik eksikliği

İlk mobil menü kodu yalnız aria-expanded ve görünürlüğü değiştiriyordu. Menü HTML'de düğmeden önceydi. Gerçek tarayıcı testinde menü açıldıktan sonra Tab basılınca odak menü yerine GitHub bağlantısına geçti (insideNav: false). Çözüm: açılışta navigation.querySelector('a')?.focus() çağrısı. Tekrar testinde insideNav: true ve odak “Ana sayfa” oldu. Escape menüyü kapatıp odağı düğmeye döndürdü. Hatayı asistan tespit etti ve düzeltti.

Ek gizlilik incelemesi: formda action olmaması, JS çalışmazsa varsayılan GET gönderiminde alanların URL'ye taşınması riskini oluşturuyordu. CSP'ye form-action 'none' eklenerek normal gönderim engellendi. Bu ikinci düzeltme kaynak incelemesine dayanır; JS kapalı ayrı bir test yapıldığı iddia edilmez.
