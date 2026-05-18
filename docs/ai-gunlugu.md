# VulnTracker - AI Geliştirme Günlüğü

## Oturum 1 [14.05.2026] [14:00 - 15:30]

### Hedef
Proje iskeletinin oluşturulması, Application Factory mimarisinin kurulması ve temel klasör yapısının konfigüre edilmesi.

### Kullandığım Mod ve Model
* **Mod:** Plan Modu
* **Model:** Gemini 3 Pro (Antigravity)

### Verdiğim Promptlar
1. **Ana İstek:** Flask 3.x and Python 3.12 uyumlu, uzantıları (extensions) bağımsız yükleyen ve dinamik config alan bir Application Factory yapısı ve temel klasör şeması oluşturulması.

### Ajanın Önerdiği Plan
Ajan; `run.py`, `config.py`, `app/__init__.py` ve blueprint klasörlerini içeren, bağımlılıkları birbirinden ayıran modüler bir geliştirme planı sundu.

### Plan'da Sorduysam / Müdahalelerim
* Standart tek dosyalık Flask yapısı yerine gelecekte genişletilebilir olması adına **Blueprint** yapısını şart koştum.
* Hassas verilerin sızmasını önlemek için `.env` (python-dotenv) desteğinin mimariye ilk adımdan eklenmesini sağladım.

### Karşılaştığım Hatalar ve Çözümler
* Herhangi bir mimari hata alınmadı, paket bağımlılıkları pürüzsüz yüklendi.
* **Uygulama İskeleti Görseli:** Projenin ilk kurulumundaki Application Factory klasör hiyerarşisi ve temel dosya yapısı `docs/img/oturum1_proje_iskeleti.png` adıyla kanıt klasörüne mühürlenmiştir.

### Bu Oturumdan Öğrendiğim
Geleneksel Flask projelerinde sıklıkla yaşanan "Circular Import" (döngüsel içe aktarma) krizlerini önlemek için Application Factory yapısının ne kadar kritik olduğunu anladım. Projeyi en baştan modüler ve Blueprint yapısıyla kurmanın, gelecekte eklenecek siber güvenlik modülleri için temiz bir genişleme alanı sağladığını kavradım.

### Sonraki Oturum İçin Notlar
* **Oturum 2 Hedefi:** Veritabanı modellerinin SQLAlchemy 2.0 standartlarında tasarlanması.

---

## Oturum 2 [15.05.2026] [16:00 - 17:15]

### Hedef
Kullanıcı (User) ve Zafiyet (Vulnerability) veritabanı modellerinin tasarlanması, ilişkilerin kurulması ve Flask-Migrate entegrasyonu.

### Kullandığım Mod ve Model
* **Mod:** Plan Modu
* **Model:** Gemini 3 Pro (Antigravity)

### Verdiğim Promptlar
1. **Ana İstek:** `app/models.py` içinde `User` ve `Vulnerability` modellerinin tanımlanması. Kullanıcılar ile zafiyetler arasında bire-çok (One-to-Many) ilişki kurulması.

### Ajanın Önerdiği Plan
Ajan, Flask-SQLAlchemy kullanarak modelleri tanımlamayı ve `flask db init` komutlarıyla veritabanı göç mekanizmasını (migration) başlatmayı önerdi.

### Plan'da Sorduysam / Müdahalelerim
* **Kritik Müdahale:** Ajanın eski Flask-SQLAlchemy (1.x) tarzı `db.Column` ve `db.String` önerisini reddettim. Hocanın rubriğindeki modern kodlama kuralına uymak adına **SQLAlchemy 2.0 Mapped ve mapped_column** yapısını kullanması talimatını verdim.

### Karşılaştığım Hatalar ve Çözümler
* İlk migration sırasında model ilişkisindeki `back_populates` parametresinin yazım hatasından kaynaklı kilitlenme yaşandı; manuel müdahale ile harf hatası düzeltilerek `flask db migrate` başarıyla mühürlendi.

* **Veritabanı Göçü (Migration) Görseli:** `flask db migrate` komutu sonrası veritabanında SQLAlchemy 2.0 standartlarında tabloların başarılı şekilde oluşturulduğunu gösteren terminal log çıktısı `docs/img/oturum2_database_migration.png` adıyla kanıt klasörüne mühürlenmiştir.

### Bu Oturumdan Öğrendiğim
SQLAlchemy 2.0 ile gelen tip güvenli (Type-hinted) `Mapped` mimarisinin, veri tabanı modellerini daha okunabilir kıldığını ve kod editörlerinin hata yakalama performansını artırdığını öğrendim. AI ajanlarının sıklıkla eski (1.x) dökümantasyon alışkanlıklarıyla kod üretebildiğini, bu yüzden bir mimar olarak güncel standartları (upgrade kurallarını) bilip ajanı yönlendirmenin şart olduğunu fark ettim.

### Sonraki Oturum İçin Notlar
* **Oturum 3 Hedefi:** Kullanıcı kayıt (Register) formlarının ve arayüzünün siber güvenlik temasında giydirilmesi.

---

## Oturum 3 [16.05.2026] [18:00 - 19:15]

### Hedef
Hocanın proje dökümanındaki "Prompt 5" yönergesine uygun olarak, Flask-WTF ve Bootstrap 5 tabanlı, siber güvenlik temalı kullanıcı kayıt (Register) akışını uçtan uca kurmak.

### Kullandığım Mod ve Model
* **Mod:** Plan Modu
* **Model:** Gemini 3 Pro (Antigravity)

### Verdiğim Promptlar
1. **Ana İstek:** `app/auth/forms.py` içinde `RegisterForm` oluşturulması, `routes.py` içine `/register` rotasının eklenerek şifrenin scrypt ile hash'lenmesi ve `register.html` arayüzünün base şablondan miras alacak şekilde siber temada kurulması.
2. **Tasarım ve Mimari Revizyonu:** Ajanın ilk planındaki açık sorulara istinaden, standart Bootstrap renkleri yerine 'JetBrains Mono' fontlu, neon yeşil parlayan hover efektli (`.btn-cyber`) özel CSS yazılması ve login rotasının şimdilik taslak bırakılması talimatı.
3. **Arayüz Düzeltme (Fast Modu):** Kayıt sayfasındaki başlığın harf arası boşluklarının (`letter-spacing`) dağınık durması üzerine, başlığın nizami ve okunaklı olacak şekilde `>_ Sisteme Kayıt Ol` formatına çekilmesi isteği.

### Ajanın Önerdiği Plan
Ajan, `base.html` dosyasına Bootstrap 5 CDN bağlantılerini eklemeyi, `forms.py`, `routes.py` ve `register.html` dosyalarını sıfırdan oluşturmayı içeren detaylı bir plan sundu. Şifre hashleme katmanını model üzerinden tetiklemeyi ve CSRF korumasını eklemeyi plana dahil etti.

### Plan'da Sorduysam / Müdahalelerim
* Ajanın login rotasını tamamen taşımak istemesine karşı çıktım; "küçük adımlarla ilerleme" kuralına sadık kalmak adına giriş (login) mekanizmasını Oturum 4'e bıraktım ve burayı şimdilik sadece placeholder (taslak) yapmasını istedim.
* Standart arayüz önerisini reddederek, projenin siber güvenlik odaklı ruhuna uyması için siber terminal estetiği ve özel buton gölgelendirmeleri dayattım.

### Karşılaştığım Hatalar, Çözümler ve Kanıtlar
* **Hata 1 (İdari/Çevre):** PowerShell üzerinde sanal ortamı ateşlerken `UnauthorizedAccess (Execution Policy)` hatasıyla karşılaşıldı.
  * **Çözüm:** `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` komutu işletilerek güvenlik politikası sadece mevcut terminal süreci için esnetildi ve `venv` aktif edildi.
* **Hata 2 (Mimari/Kritik):** Form doldurulup gönderildiğinde veya sayfaya erişilmek istendiğinde `Exception: Missing user_loader or request_loader` (500 Internal Server Error) hatası alındı.
* **Kanıt Görseli:** `docs/img/oturum3_hata_mesaji.png` klasöründe saklanmaktadır.
  * **Çözüm:** Ajanın Flask-Login entegrasyonu kurarken kullanıcı oturum köprüsünü eksik bıraktığı fark edildi. Dönüt verilerek `app/models.py` içerisine SQLAlchemy 2.x standartlarına uygun `db.session.get(User, int(user_id))` yapısını kullanan `@login_manager.user_loader` fonksiyonu başarıyla entegre edildi ve hata kalıcı olarak çözüldü.
 * **Çözüm Planı Görseli:** `docs/img/oturum3_cozum_plani.png` klasöründe saklanmaktadır.

### Başarılı Sonuç ve Uygulama Görseli
Arayüzdeki harf dağınıklığı giderildikten ve mimari yama yapıldıktan sonra kayıt sayfası sorunsuz şekilde ayağa kalktı:
Çalışan kayıt sayfasının nihai arayüz çıktısı `docs/img/oturum3_basarili_ui.png` adıyla kanıt klasörüne mühürlenmiştir.

### Bu Oturumdan Öğrendiğim
AI ajanlarına kısıt verildiğinde (örneğin: login'i henüz yazma), bu kısıtların bağlı olduğu diğer kütüphane mekanizmalarını (Flask-Login'in user_loader beklentisi gibi) kırabileceğini veya eksik bırakabileceğini yaşayarak tecrübe ettim. Bir mimar olarak üretilen planları ve hata loglarını (traceback) satır satır okumanın, körü körü onaylamamanın projeyi çökmekten kurtaran tek mekanizma olduğunu kavradım.

### Sonraki Oturum İçin Notlar
* **Oturum 4 Hedefi:** Tam işlevsel Kullanıcı Giriş (Login) ve Çıkış (Logout) sisteminin kurulması, session yönetiminin tamamlanması.



## Oturum 4 [16.05.2026] [20:00 - 20:30]

### Hedef
Hocanın "Prompt 6" yönergesine uygun olarak Kullanıcı Giriş (Login) ve Çıkış (Logout) akışlarının inşa edilmesi, veritabanı şifre kontrol katmanlarının kurulması ve oturum yönetiminin tamamlanması.

### Kullandığım Mod ve Model
* **Mod:** Plan Modu & Fast Modu (Çalışma zamanı hatalarının hızlı çözümü için)
* **Model:** Gemini 3 Pro (Antigravity)

### Verdiğim Promptlar
* **Ana İstek:** `LoginForm` oluşturulması, `/login` rotasında `db.session.execute(db.select(User))` yapısıyla modern veri çekilmesi, şifre kontrolü, oturum açma işlemi ve siber temalı `login.html` arayüzünün tamamlanması.

### Ajanın Önerdiği Plan
Ajan; Flask-WTF ve Flask-Login kullanarak SQLAlchemy 2.0 standartlarında güvenli bir giriş/çıkış akışı ve `register.html` ile tam uyumlu karanlık tema tasarımı önerdi, plan onaylanarak hızlıca koda dönüştürüldü.

### Karşılaştığım Hatalar, Çözümler ve Kanıtlar
* **Hata 1 (Veritabanı Eşitleme / Runtime):** Canlı test sırasında sisteme giriş veya kayıt yapılmaya çalışıldığında tarayıcıda `sqlalchemy.exc.OperationalError: no such table: users` hata ekranı patladı.
  * **Çözüm:** `flask db migrate` komutunun tabloları veritabanı dosyasına fiziksel olarak işlemediği, sadece taslak hazırladığı anlaşıldı. Terminalden `flask db upgrade` komutu tetiklenerek `users` tablosu SQLite (`vulntracker.db`) veritabanına fiziksel olarak kazındı. Sunucu `flask run --debug` ile yeniden ateşlendi.
  * **Kanıt Görseli:** Tarayıcıda yakalanan ilk veritabanı çöküş anı `docs/img/oturum4_veritabanı_senkronizasyon_hatası.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Hata 2 (Bağımlılık / Eksik Paket):** Form gönderildiğinde backend tarafında e-posta doğrulama mekanizması tetiklendi ve `Hata: E-posta doğrulama desteği için 'email_validator' paketini yükleyin.` Werkzeug istisnası alındı.
  * **Çözüm:** Flask-WTF kütüphanesinin e-posta alanlarını kontrol etmek için arka planda harici bir pakete ihtiyaç duyduğu teşhis edildi. Sunucu durduruldu, sanal ortama (`venv`) `pip install email-validator` komutuyla eksik paket enjekte edildi ve hata kalıcı olarak kırıldı.
  * **Kanıt Görseli:** Çalışma zamanında patlayan bağımlılık krizinin Werkzeug hata ekranı görüntüsü `docs/img/oturum4_email_validator_bagımlılık_hatası.png` adıyla arşive mühürlenmiştir.

### Başarılı Sonuç
Tüm bağımlılıklar ve veritabanı şeması senkronize edildikten sonra, yeni kayıt olan kullanıcı bilgileriyle sorunsuz giriş yapıldı. Sistem oturumu başarıyla açtı ve kullanıcıyı taslak ana sayfaya (`main.index`) fırlatarak ekrana güvenli bir şekilde "iskelet çalışıyor" nihai doğrulama mesajını bastı.

### Bu Oturumdan Öğrendiğim
Geliştirme ortamında kütüphanelerin bazı alt özellikleri için gizli bağımlılıklara (email-validator) ihtiyaç duyabileceğini ve bu hataların ancak canlı işlevsellik testlerinde (runtime) yakalanabileceğini gördüm. Ayrıca Git commit geçmişini mantıksal adımlara (paket kurulumu, kod geliştirme, dökümantasyon) bölmenin repoya ne kadar kurumsal bir olgunluk kattığını kavradım.

### Sonraki Oturum İçin Notlar
* **Oturum 5 Hedefi:** Oturum açmamış yetkisiz kullanıcıların zafiyet sayfalarına erişmesini engelleyecek `@login_required` dekoratör korumalarının eklenmesi ve VulnTracker ana dashboard tasarımının siber temada giydirilmesi.




## Oturum 5 [17.05.2026] [15:00 - 16:00]

### Hedef
Oturum açmamış yetkisiz kullanıcıların zafiyet sayfalarına erişmesini engelleyecek `@login_required` dekoratör korumalarının eklenmesi, veritabanı şema yapısının ve mock verilerinin doğrulanması, sisteme siber güvenlik testleri için 12 adet kurumsal zafiyet kaydının enjekte edilmesi, backend üzerinde SQLAlchemy 2.0 standartlarında Pagination & Veri Çekme motorunun kurulması ve ön yüzde zafiyet listesini cyberpunk temasıyla sunacak nizamî zafiyet panosunun (Web UI) inşa edilmesi.

### Kullandığım Mod ve Model
* **Mod:** Plan Modu & Fast Modu (Alembic krizleri ve şablon arama hatalarının hızlı çözümü için)
* **Model:** Gemini 3 Flash (Antigravity Agent)

### Verdiğim Promptlar
* **Ana İstek:** `app/templates/main/index.html` yoluna doğrudan müdahale edilerek, backend'den gelen pagination nesnesini (`vulnerabilities`) listeleyecek cyberpunk temalı ve Bootstrap 5 uyumlu bir sayfalama tablosunun yazılması, kritiklik seviyelerine göre dinamik badge'lerin yerleştirilmesi ve `@login_required` korumalı rotanın tetiklenmesi.

### Ajanın Önerdiği Plan
Ajan; veritabanı şemasındaki isimlendirme kurallarını revize etmeyi, `flask db migrate` ve `upgrade` komutlarıyla batch modunda veritabanını kararlı sürüme geçirmeyi, `seed_db.py` betiğini çalıştırarak SQLite veritabanına 1 yönetici ile 12 adet zafiyet kaydı basılmasını ve ana sayfa rotasının güncellenerek verilerin sayfa başına 10 kayıt olacak şekilde çekilmesini önerdi; plan onaylanarak kontrollü şekilde koda dönüştürüldü.

### Plan'da Sorduysam / Müdahalelerim
* Ajanın otomatik adımlarla doğrudan kod üretme planını sorguladım; planlama aşamasında mimariyi ve olası çakışmaları analiz ederek müdahaleleri kontrollü, adım adım gerçekleştirmeyi seçtim.
* Ajanın terminalden bağımsız klasör açma girişimini sorguladım çünkü otomatik oluşturulan klasör projenin kök dizinine kaçarak Flask'ın şablon motorunu kilitledi. Müdahaleyi manuel ve kontrollü yapmayı seçtim.
* Ajanın daha sonraki oturumlarda kurulacak detay sayfası mimarisi için `url_for('main.vulnerability')` linkini şimdiden enjekte etmesine karşı çıktım çünkü bu durum tarayıcıda projenin `BuildError` fırlatarak tamamen kilitlenmesine yol açtı. Linkleri geçici olarak pasif köprüye (`#`) çektirdim.

### Karşılaştığım Hatalar, Çözümler ve Kanıtlar
* **Hata 1 (Windows Güvenlik Duvarı / Terminal):** Sanal ortama (`venv`) geçiş yapılıp sunucu tetiklenmek istendiğinde işletim sisteminin varsayılan güvenlik politikaları sebebiyle `PSSecurityException` script çalıştırma engeliyle karşılaşılmıştır.
  * **Çözüm:** Terminal oturumuna özel, kalıcı sistem ayarlarını bozmayacak şekilde proses bazlı bir siber yetkilendirme uygulanmıştır. Terminalde `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` komutu icra edilerek barikat aşılmış ve sanal ortam başarıyla aktif edilmiştir.
  * **Kanıt Görseli:** Geliştirme ortamının başarıyla ayağa kalktığını gösteren terminal log çıktısı `docs/img/oturum5_flask_sunucu_aktif_ve_calisiyor.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Hata 2 (Veritabanı Göçü / UNIQUE Constraint):** SQLite veritabanında model güncellemeleri esnasında isimlendirilmemiş kısıt kuralları sebebiyle `ValueError: Constraint must have a name` göç mimarisi barikatı patlamıştır.
  * **Çözüm:** `app/__init__.py` (veya veritabanı metadata seviyesinde) isimlendirme konvansiyonu (`naming_convention`) tanımlanarak tüm benzersiz anahtar ve kısıtlara kurumsal adlandırma kuralları otomatik atanmış ve hata ezilmiştir.
  * **Kanıt Görseli:** Veritabanı şemasının göçü esnasında SQLite mimarisinin fırlattığı kurumsal hata ekranı `docs/img/oturum5_alembic_constraint_must_have_name_hatası.png` adıyla arşive mühürlenmiştir.
* **Hata 3 (Veritabanı Göçü / SQLite Batch):** SQLite veritabanının tablo sütun düşürme/ekleme operasyonlarındaki kısıtlamaları sebebiyle göç işlemi sırasında çoklu değer işleme krizine girilmiş ve sistem kilitlenmiştir.
  * **Çözüm:** `migrations/env.py` dosyasında `context.configure(..., render_as_batch=True)` ayarı aktifleştirilerek tabloların batch modunda taşınması sağlanmış, `flask db migrate` ve `flask db upgrade` başarıyla tamamlanmıştır.
  * **Kanıt Görseli:** Karşılaşılan çoklu değer/batch işleme krizinin teknik analiz safhası `docs/img/oturum5_alembic_multiple_values_render_as_batch_hatası.png` adıyla, kriz aşıldıktan sonraki başarılı göç çıktısı ise `docs/img/oturum5_basarili_veritabanı_build_ve_migration.png` adıyla mühürlenmiştir.
* **Hata 4 (Flask Şablon Algılama / Klasör Sapması):** Ajanın otomatik klasör açma girişimindeki sapma sebebiyle sunucu yeni yazılan `index.html` dosyasını algılayamamış ve tarayıcıda sürekli eski test metnini render etmeye devam etmiştir.
  * **Çözüm:** Dosya ağacı üzerinde milimetrik bir denetim gerçekleştirilerek kök dizine kaçmış olan hatalı klasör yapıları temizlenmiş, zafiyet tablosunu barındıran şablon dosyası nizamî olarak `app/templates/main/index.html` konumuna yerleştirilmiş ve Flask sunucusu yeniden başlatılmıştır.
  * **Kanıt Görseli:** Ajanın geliştirme esnasında önerdiği adımların denetlendiği o kritik sorgulama anı `docs/img/oturum5_ajan_planini_sorgulama_ve_mudahale.png` adıyla klasöre mühürlenmiştir.
* **Hata 5 (Arayüz Derleme / URL İnşa):** Rota bağlantısı nizamî kurulduktan sonra tarayıcı yenilendiğinde, henüz sistem mimarisinde tanımlanmamış bir endpoint'e yönlendirme yapıldığı için Werkzeug `BuildError` hatası fırlamıştır.
  * **Çözüm:** Tablodaki "Detay" butonlarının `url_for('main.vulnerability')` çağrısı yaptığı, ancak bu rotanın henüz backend tarafında çizilmediği teşhis edilmiştir. Arayüzün kilitlenmesini engellemek adına ilgili butonların link yapıları geçici olarak güvenli pasif köprü (`href="#"`) moduna çekilerek hata kalıcı olarak kırılmıştır.
  * **Kanıt Görseli:** Ön yüz şablon motorunda kilitlenmeye yol açan Werkzeug arayüz analiz ekranı `docs/img/oturum5_jinja2_url_build_error.png` adıyla arşive mühürlenmiştir.

### Başarılı Sonuç
Tüm veritabanı kısıtları, klasör hiyerarşileri ve yönlendirme linkleri optimize edildikten sonra, `vulntracker.db` veritabanındaki 12 adet kurumsal mock zafiyetin ilk 10 tanesi siber operasyon merkezi standartlarına uygun cyberpunk/minimalist temayla ön yüze kusursuz şekilde aktı. Ters sıralama mantığı doğrulanarak en güncel açıklar en üste dizildi ve alt taraftaki modern sayfalama navigasyonu (Pagination) tıkır tıkır çalışarak sistemi sıfır hata ile ayağa kaldırdı.
* **Kanıt Görseli:** Başarıyla ayağa kalkan ve sayfalama navigasyonu doğrulanan nihai zafiyet panosu ekranı `docs/img/oturum5_zafiyet_paneli_sayfalama_ve_arayuz_dogrulama.png` adıyla kanıt klasörüne mühürlenmiştir.

### Bu Oturumdan Öğrendiğim
Modern Flask mimarilerinde Blueprint yapılanmaları kurulurken şablon dosyalarının aranma öncelikleri ve klasör hiyerarşilerinin ne kadar milimetrik ayarlanması gerektiğini öğrendim. SQLite veritabanlarında Alembic ile göç (migration) süreçlerini işletirken, isimlendirilmemiş constraint kurallarının ve standart göç komutlarının sistemi kilitleyebileceğini; bu durumların `naming_convention` ve `render_as_batch` mimari müdahaleleriyle nasıl esnetileceğini uygulamalı olarak tecrübe ettim. Ayrıca zafiyet panolarında siber olay müdahale süreçlerinin hızı için verilerin `ID DESC` mantığıyla çekilmesinin analist standardı olduğunu kavradım.

### Sonraki Oturum İçin Notlar
* **Oturum 6 Hedefi:** Sisteme yeni zafiyet ekleme, mevcut zafiyetlerin detayına girip bilgilerini güncelleme ve geçersiz zafiyetleri sistemden tamamen silebilme (CRUD) özelliklerinin backend ve ön yüz form altyapılarının inşa edilmesi.










## Oturum 6 [18.05.2026] [11:00 - 12:30]

### Hedef
Platformun çekirdek fonksiyonel motoru olan **Zafiyet Yönetimi (CRUD - Create, Read, Update, Delete)** altyapısının backend ve ön yüz seviyesinde inşa edilmesi; yeni zafiyet ekleme, mevcut kayıtların detayını güvenli çekip düzenleme ve silme rotalarının try-except/rollback zırhlarıyla veritabanına kilitlenmesi, iki ayrı HTML yükü yerine dinamik kendini uyarlayan tek bir cyberpunk form şablonunun (`vulnerability_form.html`) ön yüze entegre edilmesi ve Oturum 5'te pasif bırakılan "Detay" köprülerinin bu yeni CRUD motoruna bağlanarak sistemin uçtan uca doğrulanması.

### Kullandığım Mod ve Model
* **Mod:** Act Modu & Antigravity Panel Denetimi (Donma krizleri ve lojistik kopuklukların manuel müdahaleyle çözülmesi için)
* **Model:** Gemini 3 Flash (Antigravity Agent)

### Verdiğim Promptlar
* **Ana İstek:** `app/main/__init__.py` içerisine zafiyet ekleme, düzenleme ve silme işlevlerini üstlenecek rotaların modern SQLAlchemy 2.0 select mimarisiyle yazılması. Yazılan kodların defansif derinlik (Defense in Depth) standartlarına uygun olarak try-except bloklarıyla korunması, hata anında `db.session.rollback()` çalıştırılması ve ön yüzde tek bir `vulnerability_form.html` şablonunun siber punk/SOC terminal estetiğiyle ayağa kaldırılması.

### Ajanın Önerdiği Plan
Ajan; ilk olarak `Flask-WTF` form yapısını doğrulamayı, ardından backend üzerinde üç ana CRUD rotasını kurmayı, ön yüzde ekleme ve düzenleme sayfaları için iki ayrı şablon dosyası açmayı planladı. Ancak analist süzgeciyle yapılan mimari oyun kurma ve müdahaleler neticesinde ajanın planı revize edilerek Clean Code çizgisine çekildi.

### Plan'da Sorduysam / Müdahalelerim
* Ajanın veritabanı commit işlemlerini doğrudan yalın ve korumasız halde çakma planını sorguladım. SQLite yazma/silme anında yaşanacak anlık kilitlenmelerde sunucunun 500 Internal Error vererek stack trace sızıntısı üretmesini engellemek için tüm commit operasyonlarına `try-except` zırhı giydirip `except` anında `db.session.rollback()` tetiklettim.
* Ajanın ekleme ve düzenleme işlemleri için iki ayrı HTML şablonu (`create_vulnerability.html` ve `edit_vulnerability.html`) üretme planına karşı çıktım. Dosya yükünü ve kod tekrarını engellemek adına tek bir ortak `vulnerability_form.html` yazdırarak, içeriğe gelen nesne durumuna göre arayüzün dinamik şekillenmesini zorunlu kıldım.
* Geliştirme esnasında yapay zeka ajanının 10 dakika boyunca loading ekranında kalıp donması/kilitlenmesi üzerine sürece manuel müdahale ettim, onay tetiğini el ile çekerek repoyu kurtardım. Ajanın kilitlenme sebebiyle eksik bıraktığı o son lojistik köprüyü, yani `index.html` üzerindeki pasif `href="#"` linklerini el ile yeni yazdığımız edit rotasına dinamik olarak (`url_for('main.edit_vulnerability', vuln_id=vuln.id)`) bağladım.

### Karşılaştığım Hatalar, Çözümler ve Kanıtlar
* **Hata 1 (Form Yapılandırma ve Onay Kısıtı):** Ajanın ön yüz ile backend arasındaki veri dezenfeksiyonunu tam doğrulamadan doğrudan şablonlara atlama eğilimi siber denetime takılmıştır.
  * **Çözüm:** `app/main/forms.py` dosyası üzerinde milimetrik denetim yapılarak girdilerin karakter sınırları ve `SelectField` tip kısıtlamaları kilitlenmiş, ajandan tam kod onayı alınmıştır.
  * **Kanıt Görseli:** Form mimarisinin kurumsal nizamda başarıyla oluşturulduğunu gösteren ilk teftiş anı `docs/img/oturum6_forms_py_kod_incelemesi.png` adıyla arşive mühürlenmiştir.
* **Hata 2 (Backend Commit Korumasızlığı / Veri Güvenliği):** CRUD rotalarında `db.session.commit()` komutlarının herhangi bir hata yakalama mekanizması olmadan çıplak bırakıldığı teşhis edilmiştir.
  * **Çözüm:** Olası SQLite kilitlenmelerine ve veri zehirlenmelerine karşı backend rotaları defansif programlama ilkeleriyle güncellenmiş, işlem başarısız olduğunda oturumu güvenli şekilde geri alan `rollback` komutları enjekte edilmiştir.
  * **Kanıt Görseli:** Backend rotaları yapılandırılırken siber güvenlik açıklarının tarandığı o ilk hazırlık safhası `docs/img/oturum6_backend_rotalari_try_except_zirhi.png` adıyla mühürlenmiştir.
* **Hata 3 (Geliştirme Paneli Senkronizasyon Kaybı / Donma):** Ön yüz şablon derlemesine geçileceği sırada Antigravity Agent arka plan senkronizasyon krizine girmiş ve arayüz 10 dakika boyunca loading durumunda kilitli kalmıştır.
  * **Çözüm:** Oturum manuel olarak onaylanmış, ajanın yarıda bıraktığı kod yapısı analist tarafından el ile devralınarak Jinja2 entegrasyon köprüleri eksiksiz olarak tamamlanmıştır.
  * **Kanıt Görseli:** Ajanın donma öncesinde rotaları işleyip şablon aşamasına geçmeye çalıştığı o lojistik kırılma anı `docs/img/oturum6_dinamik_override_record_butonu.png` adıyla klasöre mühürlenmiştir.
* **Hata 4 (Yetkisiz HTTP İstek Manipülasyonu / Sızma Girişimi):** Oturum açmamış siber aktörlerin veya botların URL satırından doğrudan `/vulnerability/add` rotasını çağırarak sisteme sahte veri basma riski (IDOR/Erişim Kontrolü İhlali) analiz edilmiştir.
  * **Çözüm:** Rotaların tepesine `@login_required` zırhı çakılmış ve yerel sunucuda gizli sekme açılarak sızma testi icra edilmiştir. Sistemin yetkisiz isteği havada yakalayarak HTTP 302 yönlendirmesiyle Giriş ekranına fırlattığı ve neon mavisi kurumsal uyarı bastığı doğrulanmıştır.
  * **Kanıt Görseli:** Gizli sekmeden yapılan sızma girişiminin siber bir kale gibi engellendiği o anın canlı test kanıtı `docs/img/oturum6_yetkisiz_erisim_barikati.png` adıyla mühürlenmiştir.

### Başarılı Sonuç
İnatçı yapay zeka donmalarına ve mimari eksikliklere rağmen manuel müdahaleyle ayağa kaldırılan CRUD motoru %100 başarıyla doğrulandı. Tek bir esnek şablondan veritabanı durumuna göre; ekleme modunda yeşil neon renkli `[ EXECUTE_INSERT ]`, düzenleme modunda ise turuncu neon renkli `[ OVERRIDE_RECORD ]` butonlarını render eden dinamik ön yüz kusursuz çalıştı. `db.get_or_404` seçimiyle sahte ID manipülasyonları elendi, try-except zırhlarıyla Flask'ın çökme riskleri sıfırlandı ve ana panodaki detay butonları yeni motora nizamî olarak bağlandı. Proje repoya push edilmeye hazır kararlı sürüme ulaştı.

### Bu Oturumdan Öğrendiğim
Geliştirme süreçlerinde yapay zeka ajanlarının zaman zaman senkronizasyon kaybı yaşayıp donabileceğini, bu gibi durumlarda siber analistin kontrolü eline alıp manuel müdahale (Incident Response) yapmasının projeyi lojistik olarak nasıl kurtardığını öğrendim. Backend operasyonlarında hata sızıntısını ve stack trace sızıntılarını önlemek adına `db.get_or_404` kullanmanın kurumsal önemini, veritabanı kilitlenmelerine karşı defansif programlamanın (`rollback`) hayat kurtardığını uygulamalı olarak gördüm. Ayrıca Clean Code standartları gereği ön yüzde dinamik şablon yönetiminin kod karmaşasını nasıl yarı yarıya azalttığını tecrübe ettim.

### Sonraki Oturum İçin Notlar
* **Oturum 7 Hedefi:** Projenin ana görsel anayasasını oluşturacak olan **Base Template (Jinja2 Kalıpları) ve Frontend Tasarımı (UI/UX) Entegrasyonu** safhasına geçilmesi. Tüm alt şablonların mirasını devralacağı ana omurganın (`app/templates/base.html`) sıfırdan inşa edilmesi; sayfalar arası dinamik başlık ve içerik bloklarının kilitlenmesi, sistem genelinde fırlatılan tüm siber uyarıları (flash mesajları) Bootstrap 5 `alert-dismissible` neon kutularıyla karşılayacak global mesaj motorunun kurulması, üst menüde projenin siberpunk logosunu ve o an oturumu açık olan sistem analistinin dinamik profil verilerini (`current_user.username`) işleyecek SOC terminal arayüz tasarımlarının responsive (duyarlı) şekilde giydirilmesi.







## Oturum 7 [18.05.2026] [12:35 - 15:10]

### Hedef
Projenin ana görsel anayasasını oluşturacak Base Template (Jinja2 Kalıpları) ve Frontend Tasarımı (UI/UX) Entegrasyonu safhasının icra edilmesi. Zafiyet Yönetim Matrisinin mantıksal eksikliklerinin (Silme motoru ve aktif/çözülmüş durum kontrolü) ve Türkiye yerel saatiyle (UTC+3) senkronize işleyen dinamik zaman damgalarının backend katmanına kilitlenmesi. Çift tablolu yapının arayüzde yarattığı dikey kalabalığın dezenfekte edilerek çözülmüş zafiyetlerin tamamen bağımsız ve izole bir arşiv sayfasına (`archived_index.html`) taşınması.

### Kullandığım Mod ve Model
* **Mod:** Otonom Refaktör, Sistem Entegrasyonu & UX Dezenfeksiyon Modu
* **Model:** Claude 3.5 Sonnet & Gemini 3 Flash (Kompozit Mühimmat Geçişi)

### Verdiğim Promptlar
1. **Ana İstek:** `base.html` dosyasının dinamik terminal promptu ile kurulması, `Vulnerability` modeline `is_resolved` alanının enjekte edilmesi, düzenleme formuna kırmızı neon silme butonunun giydirilmesi ve çift tablonun iptal edilerek arşivi listeleyen bağımsız bir `archived_index` rotasının otonom olarak inşa edilmesi.

### Ajanın Önerdiği Plan
Ajan; genel şablon omurgasını kurmayı, durum yönetiminde 3 adımlı stratejik planı ve arşiv geçişi için otonom yazma rotasını içeren bir refaktör planı sundu.

### Plan'da Sorduysam / Müdahalelerim
* Ajanın arayüz linkini kolay yoldan değiştirme eğilimini reddedip backend'deki fonksiyon adını kurumsal standardımız olan `add_vulnerability` çizgisine kilitledim.
* Claude Sonnet'in arşiv planında eski navigasyon linkine (`new_vulnerability`) sapma eğilimini fark ederek kod yazım aşamasına geçilmeden önce havada kilitledim.
* Ajanlara tam ekran kod döktürmek yerine, plan onaylandıktan sonra arka plandaki yazma motoruyla dosyaları doğrudan güncellettim.

### Karşılaştığım Hatalar ve Çözümler
* Veritabanına yeni alan eklenince alınan `OperationalError` hatası, aktif `instance/vulntracker.db` dosyasının tespiti ve el ile fiziksel imhası sonrası `db.create_all()` tetiklenerek çözüldü.
* Ajanın kök dizindeki sahte `app.db` dosyasını silmeye çalışması engellenerek doğru veritabanı deşifre edildi.
* Arka plan otonom yazma motorunun işlem limitine toslaması krizinde inisiyatif alınarak Claude Sonnet'e geçiş yapıldı.
* Arşiv sayfası oluşturulurken alınan `TemplateNotFound` hatası, otonom motorun dosyayı doğru fiziksel konuma mühürlemesi emredilerek çözüldü.
* **Zafiyet Silme Motoru Görseli:** Silme işleminin güvenli şekilde arayüze eklenmesi planı `docs/img/oturum7_01_zafiyet_silme_motoru_plani.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Durum Yönetimi Görseli:** is_resolved bayrağının model ve form katmanlarında projelendirilmesi `docs/img/oturum7_02_durum_yonetimi_arayuz_plani.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Veritabanı Şema Hatası Görseli:** SQLite sütun eksikliği sebebiyle fırlatılan kriz anı `docs/img/oturum7_03_veritabanı_sema_hatasi.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Aktif Veritabanı Keşfi Görseli:** Ajanın silemediği aktif veritabanı dosyasının tespiti `docs/img/oturum7_04_aktif_veritabani_kesfi.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Ajan Kota Kesintisi Görseli:** Otonom motorun limitlere takıldığı an `docs/img/oturum7_05_ajan_kota_kesintisi.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Çift Tablo Denetimi Görseli:** Alt tablonun iptal edilerek izole arşiv sayfasına geçiş kararı `docs/img/oturum7_06_pano_cift_tablo_denetimi.png` adıyla kanıt klasörüne mühürlenmiştir.
* **Şablon Bulunamadı Görseli:** Dosya yolunun yanlış konuma yazılmasıyla alınan hata logu `docs/img/oturum7_07_sablon_bulunamadi_hatasi.png` adıyla kanıt klasörüne mühürlenmiştir.

### Bu Oturumdan Öğrendiğim
Geliştirme süreçlerinde yapay zeka ajanlarının kota veya sistemsel I/O kilitlenmelerine çarptığı kriz anlarında siber analist refleksleriyle local terminale ve diske doğrudan müdahale etmenin operasyon kurtarmadaki hayati önemini gördüm. SQL tabanlı veritabanlarında şema değişikliklerinde diski fiziksel olarak temizlemek veya doğru dosya adına nokta atışı operasyon yapmak gerektiğini tecrübe ettim. Ayrıca kurumsal SOC arayüzlerinde tüm verileri tek sayfaya yığmanın UX odağını dağıttığını, izole sayfa mimarisinin analist konforunu üst seviyeye çıkardığını yaşayarak kavradım.

### Sonraki Oturum İçin Notlar
* **Oturum 8 Hedefi:** Sistemin ikinci büyük kalesi olan Kullanıcı Kimlik Doğrulama (Authentication - Auth Blueprint) ve Giriş/Kayıt Sayfalarının Siberpunk UI/UX Entegrasyonu safhasına geçilmesi.




