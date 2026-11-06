# Jahan Teymurlu - Kişisel Web Portfolyosu

Dijital Oyun Tasarımı · GEP1316 · Ara Değerlendirme Ödevi 2

## Yayın durumu

**GitHub Pages yayını henüz yapılmadı.** Aşağıdaki adres yayın hedefidir; doğrulanmış canlı site bağlantısı değildir:

`https://anpunabis.github.io/gep1316-portfolyo/`

Hedef depo: `https://github.com/Anpunabis/gep1316-portfolyo` (oluşturulması gerekiyor). GitHub profili ve üç mevcut proje deposu tarayıcıda doğrulandı; hesaba giriş yapılmadığı için yeni depo/yayın oluşturulmadı. Yayından sonra bu bölüme GitHub'ın gösterdiği gerçek canlı adresi ekleyin ve linkleri kontrol edin.

## Açma

ZIP'i çıkarın. **index.html** dosyasına çift tıklayın. Web sitesi için Python, Node.js veya paket kurulumu gerekmez. Tarayıcı yeterlidir. Tema tercihi bazı tarayıcılarda yerel dosya açılışında sayfalar arasında taşınmayabilir; yayınlanmış sitede aynı origin altında saklanır. Mesaj kopyalama engellenirse metni elle seçebilirsiniz.

Yerel sunucu kullanmak isterseniz bu klasörde `python -m http.server 8000` çalıştırıp `http://localhost:8000/` adresini açabilirsiniz. Python sadece bu isteğe bağlı sunucu içindir.

## Sayfalar ve özellikler

- `index.html`: Tanıtım, JT avatarı, seçilmiş projeler.
- `hakkimda.html`: Eğitim, ilgi alanları, kodlama ve YZ'nin meslekteki yeri.
- `projeler.html`: 7 kart, kategori filtresi, Türkçe arama, sonuç sayacı.
- `iletisim.html`: Doğrulanan, erişilebilir mesaj taslağı formu ve GitHub profili.
- `projeler/`: 7 proje ayrıntısı; üç yeni demo tarayıcıda çalışır.
- `style.css` ve `script.js`: Ortak tasarım ve davranışlar. Harici bağımlılık yok.
- `assets/`: Yerel SVG avatar ve proje şemaları. Gerçek oyun ekran görüntüsü olarak sunulmaz.
- `indir/`: İlk Python projesi, güncel raporuyla birlikte ZIP olarak ve main.py kaynağı.
- `belgeler/`: Üç cihaz görüntüsü, form görüntüleri, yerleşim ve kontrast test kayıtları.
- `RAPOR.pdf` / `RAPOR.md`: 3 sayfalık süreç raporu ve düzenlenebilir metni.
- `PROMPTLAR.md`: Gerçek sohbet girdileri ve altı geliştirme istemi çalışma kaydı.
- `TESTLER.md`: Etkileşim, erişilebilirlik, gizlilik ve form testleri.

JavaScript etkileşimleri: tema ve tercihin saklanması; mobil menü ve Escape; kategori filtresi; arama ve sonuç sayacı; form doğrulaması; mesaj uzunluğu sayacı; güvenli taslak önizleme; metin kopyalama; dallanan hikâye; denge hesabı; seviye aşaması seçimi.

## GitHub Pages'e yayınlama

1. Anpunabis hesabında `gep1316-portfolyo` adlı bir depo oluşturun. Ücretsiz hesapta Pages için public depo kullanılabilir.
2. Bu klasörün **içeriğini** depoya yükleyin. index.html doğrudan depo kökünde olmalı; fazladan GEP1316_Odev2_JahanTeymurlu klasörünün içinde kalmamalı. .nojekyll dosyası da dahil edilebilir.
3. Settings > Pages > Build and deployment > Source bölümünde **Deploy from a branch** seçin.
4. Dal olarak **main**, klasör olarak **/(root)** seçip Save'e basın.
5. GitHub'ın oluşturduğu adres açılınca siteyi, proje indirmelerini ve menüleri kontrol edin. Bu README'ye doğrulanan canlı adresi yazın.
6. Teams teslimine ZIP, rapor ve canlı site/depo bağlantılarını ekleyin.

Resmî kaynak: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Proje kökeni ve tamamlanacak içerik

Oyun Atölyesi birinci ara değerlendirme projesidir. Ball_Project, VFX_CarGame ve Some_Github_Project kullanıcının verdiği GitHub profilinde doğrulanan mevcut depolardır. Son Sinyal, Denge Laboratuvarı ve Bir Seviyenin Ritmi bu portfolyo için yeni üretildi. Mevcut depoların GEP1316 Ödev 1–6 kapsamına ait oldukları doğrulanmadı. Bu nedenle dört adet GEP1316 ders çalışması şartının bütünüyle tamamlandığı iddia edilmez. Öğrenci asıl ders çalışmalarını ve bunlara ait kendi “ne öğrendim” cümlelerini eklemeli veya mevcut projelerin uygunluğunu öğretmeniyle netleştirmelidir.

Prompt belgesindeki altı geliştirme kaydı, öğrencinin ayrı ayrı gönderdiği altı mesaj değildir; bu ayrım açıkça yazılıdır. Gerçek öğrenci istemlerini ve kendi kabul/red/düzenleme kararlarını günlüğe ekleyin. Yansıtma, öğrencinin verdiği “kodlama bilgim zaten vardı, zor gelmiyordu; ders bana çok şey öğretti” bilgisine dayanarak YZ desteğiyle yazıldı; okuyup doğruluğunu kontrol edin.

## Gizlilik ve güvenlik

Form mesaj **göndermez** ve sunucuya veri kaydetmez. Kişisel telefon veya adres yoktur. Yalnız tema tercihi localStorage'da tutulur. Üçüncü taraf font, betik, analiz veya izleyici yoktur. GitHub bağlantıları dış sayfadır. Kullanıcı girdisi innerHTML yerine textContent ile gösterilir. CSP içindeki form-action 'none', JavaScript devre dışı kalsa bile normal form gönderimini engeller. Bu kaynak incelemesiyle doğrulandı; JavaScript kapalı ayrı tarayıcı testi yapılmadı.

## Doğrulama

11 sayfa × 3 görünüm = 33 yerleşim kontrolü (390×844, 768×1024, 1440×1000) başarılı. Gerçek tarayıcı ekran görüntüleri belgeler klasöründedir. Form, arama/filtre, tema, mobil menü, üç hikâye sonu ve hesaplama araçları tarayıcıda denendi. Yerel bağlantılar, alt metinler, form etiketleri, sayfa başlıkları ve kontrast oranları kontrol edildi. Gerçek mobil donanım veya tüm tarayıcılarla test yapıldığı iddia edilmez.
