from django.db import models

class KayanHaberler1Enustsol(models.Model):
    Baslik = models.CharField('Başlık', max_length=50)
    resim = models.FileField(upload_to='img/',null=True)
    Linkto = models.CharField('bağlantı adresi (boş olabilir)', max_length=50, blank=True)
    önyazi = models.CharField('altyazı', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()
    def __str__(self):
        return self.Baslik


    class Meta:
        verbose_name = 'Kayan Haberler 1 En Üst Sol'
        ordering = ['-dimDate']  # sorted news by dimdate

class KayanHaberler1EnustSag(models.Model):
    Baslik = models.CharField('Başlık', max_length=50)
    resim = models.FileField(upload_to='img/',null=True)
    Linkto = models.CharField('bağlantı adresi (boş olabilir)', max_length=50, blank=True)
    önyazi = models.CharField('altyazı', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()
    def __str__(self):
        return self.Baslik


    class Meta:
        verbose_name = 'Kayan Haberler 1 En Üst Sağ'
        ordering = ['-dimDate']  # sorted news by dimdate

class TarihteBugun(models.Model):
    Baslik=models.CharField('Baslik',max_length=100)
    OnYazı=models.TextField('ÖnYazı',max_length=5000)
    Araresim=models.FileField('Araresim', blank=True, null=True, upload_to='img/araresim/')
    Yazı=models.TextField('AsılMetin',max_length=9000)
    Yayıntarih = models.DateTimeField(auto_now_add=True)  # timezone.now()
    def __str__(self):
        return self.Baslik

    class Meta:
        verbose_name = 'Tarihte Bugün'
        ordering = ['-Yayıntarih']



class Haberler(models.Model):
    Baslık = models.CharField('Haber başlığı', max_length=80)
    Haber_Detay = models.TextField('haber detayları', max_length=5000)
    anasayfa_resm=models.FileField('Anasayfa Kayar Kısımda Görüntülenecek Fotoğrafı Yükleyiniz"/static/img/xxx.xx"Biçim', blank=True, null=True, upload_to='img/')
    # obviously it is what it looks like.
    resm1 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"Biçim', blank=True, null=True, upload_to='img/')
    resm12 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"Biçim', blank=True, null=True, upload_to='img/')
    resm13 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"Biçim', blank=True, null=True, upload_to='img/')
    resm14 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"Biçim', blank=True, null=True, upload_to='img/')
    resm15 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"Biçim', blank=True, null=True, upload_to='img/')
    Görüntüleme = models.IntegerField('Görüntüleme')
    HaberCesiti = [
        ('Ekonomi', 'Ekonomi'),
        ('İslam', 'İslam'),
        ('Savaş', 'Savaş'),
        ('Teknoloji', 'Teknoloji'),
        ('Gündelik', 'Gündelik'),
        ('Dünya', 'Dünya'),
        ('OrtaDoğu', 'OrtaDoğu'),
    ]
    HaberTur=models.CharField(max_length=50,choices=HaberCesiti,default='İslam')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Baslık
    class Meta:
        verbose_name = 'Haberler'
        ordering = ['-dimDate']
class İşHaber(models.Model):
    newsTitle = models.CharField('İş Başlığı', max_length=50)
    newsDetail = models.TextField('İş Detayları', max_length=5000)
    # obviously it is what it looks like.
    imgShow = models.FileField(
        'İş sorgulama sayfasını gösteren resim', blank=True, null=True, upload_to='img/')

    upLoadImg = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg2 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg3 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg4 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg5 = models.FileField(
        'Haberdeki resmi yükleyin, lütfen referans resmi kullanın"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')

    viewedTimes = models.IntegerField('Görüntüleme')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.newsTitle

    class Meta:
        verbose_name = 'İş danışmanlığı'
        ordering = ['-dimDate']  # sorted news by dimdate

class Kullanıcı(models.Model):
    Kullanıcı_adı = models.CharField('Kullanıcı adı', max_length=50)
    parola = models.CharField('parola', max_length=50)
    mail = models.EmailField('e-posta',max_length=500)

    class Meta:
        verbose_name = 'Kullanıcı bilgisi'
class Gündem(models.Model):
    Baslik=models.CharField('Başlık',max_length=80)
    metin=models.TextField('metin',max_length=200)
    Tarih = models.DateTimeField(auto_now_add=True)  # timezone.now()
    class Meta:
        verbose_name = 'Kullanıcı bilgisi'
        ordering = ['-Tarih']
class SonDakikaHBR(models.Model):
    Baslik=models.CharField('Başlık',max_length=80)
    Fotograf1 =models.FileField('Birinci Fotoğraf',blank=True, null=True, upload_to='img/SonDakika/')
    FotoğrafArasıMetin = models.TextField('FotoğrafArasıMetin', max_length=200,null=True)
    Fotograf2 = models.FileField('İkinci fotoğraf Fotoğraf', blank=True, null=True, upload_to='img/SonDakika/')
    FotoğrafArasıMetin2 = models.TextField('FotoğrafArasıMetin', max_length=200,null=True)
    Fotograf3 = models.FileField('Üçüncü Fotoğraf Fotoğraf', blank=True, null=True, upload_to='img/SonDakika/')
    metin=models.TextField('metin',max_length=200,null=False)
    Tarih = models.DateTimeField(auto_now_add=True)  # timezone.now()
    def __str__(self):
        return self.Baslik
    class Meta:
        verbose_name = 'Son Dakika'
        ordering = ['-Tarih']