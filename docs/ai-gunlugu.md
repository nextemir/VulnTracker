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
 * **Kanıt Görseli:** ![Hata Mesajı](./img/oturum3_hata_mesaji.png)
  * **Çözüm:** Ajanın Flask-Login entegrasyonu kurarken kullanıcı oturum köprüsünü eksik bıraktığı fark edildi. Dönüt verilerek `app/models.py` içerisine SQLAlchemy 2.x standartlarına uygun `db.session.get(User, int(user_id))` yapısını kullanan `@login_manager.user_loader` fonksiyonu başarıyla entegre edildi ve hata kalıcı olarak çözüldü.
 * **Çözüm Planı Görseli:** ![Çözüm Planı](./img/oturum3_cozum_plani.png)

### Başarılı Sonuç ve Uygulama Görseli
Arayüzdeki harf dağınıklığı giderildikten ve mimari yama yapıldıktan sonra kayıt sayfası sorunsuz şekilde ayağa kalktı:
![Çalışan Kayıt Sayfası](./img/oturum3_basarili_ui.png)

### Bu Oturumdan Öğrendiğim
AI ajanlarına kısıt verildiğinde (örneğin: login'i henüz yazma), bu kısıtların bağlı olduğu diğer kütüphane mekanizmalarını (Flask-Login'in user_loader beklentisi gibi) kırabileceğini veya eksik bırakabileceğini yaşayarak tecrübe ettim. Bir mimar olarak üretilen planları ve hata loglarını (traceback) satır satır okumanın, körü körü onaylamamanın projeyi çökmekten kurtaran tek mekanizma olduğunu kavradım.

### Sonraki Oturum İçin Notlar
* **Oturum 4 Hedefi:** Tam işlevsel Kullanıcı Giriş (Login) ve Çıkış (Logout) sisteminin kurulması, session yönetiminin tamamlanması.