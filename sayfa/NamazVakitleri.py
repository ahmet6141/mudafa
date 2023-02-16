import requests
from bs4 import BeautifulSoup
import urllib3
import lxml

headers =  {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

trabzon = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9905/trabzon-icin-namaz-vakti"
istanbul="https://namazvakitleri.diyanet.gov.tr/tr-TR/9541/istanbul-icin-namaz-vakti"
bursa="https://namazvakitleri.diyanet.gov.tr/tr-TR/9335/bursa-icin-namaz-vakti"
çanakkale="https://namazvakitleri.diyanet.gov.tr/tr-TR/9352/canakkale-icin-namaz-vakti"
kocaeli="https://namazvakitleri.diyanet.gov.tr/tr-TR/9654/kocaeli-icin-namaz-vakti"
konya="https://namazvakitleri.diyanet.gov.tr/tr-TR/9676/konya-icin-namaz-vakti"
eskişehir="https://namazvakitleri.diyanet.gov.tr/tr-TR/9470/eskisehir-icin-namaz-vakti"
adana="https://namazvakitleri.diyanet.gov.tr/tr-TR/9146/adana-icin-namaz-vakti"
adıyaman="https://namazvakitleri.diyanet.gov.tr/tr-TR/9158/adiyaman-icin-namaz-vakti"
ardahan="https://namazvakitleri.diyanet.gov.tr/tr-TR/9238/ardahan-icin-namaz-vakti"
ağrı="https://namazvakitleri.diyanet.gov.tr/tr-TR/9185/agri-icin-namaz-vakti"
samsun="https://namazvakitleri.diyanet.gov.tr/tr-TR/9819/samsun-icin-namaz-vakti"
edirne="https://namazvakitleri.diyanet.gov.tr/tr-TR/9419/edirne-icin-namaz-vakti"
tekirdağ="https://namazvakitleri.diyanet.gov.tr/tr-TR/9879/tekirdag-icin-namaz-vakti"
tokat="https://namazvakitleri.diyanet.gov.tr/tr-TR/9887/tokat-icin-namaz-vakti"
bolu="https://namazvakitleri.diyanet.gov.tr/tr-TR/9315/bolu-icin-namaz-vakti"
çorum="https://namazvakitleri.diyanet.gov.tr/tr-TR/9370/corum-icin-namaz-vakti"
karabük="https://namazvakitleri.diyanet.gov.tr/tr-TR/9581/karabuk-icin-namaz-vakti"
kilis="https://namazvakitleri.diyanet.gov.tr/tr-TR/9629/kilis-icin-namaz-vakti"
kastamonu="https://namazvakitleri.diyanet.gov.tr/tr-TR/9609/kastamonu-icin-namaz-vakti"
denizli="https://namazvakitleri.diyanet.gov.tr/tr-TR/9392/denizli-icin-namaz-vakti"
afyonkarahisar="https://namazvakitleri.diyanet.gov.tr/tr-TR/9167/afyonkarahisar-icin-namaz-vakti"
aksaray="https://namazvakitleri.diyanet.gov.tr/tr-TR/9193/aksaray-icin-namaz-vakti"
amasya="https://namazvakitleri.diyanet.gov.tr/tr-TR/9198/amasya-icin-namaz-vakti"
ankara="https://namazvakitleri.diyanet.gov.tr/tr-TR/9206/ankara-icin-namaz-vakti"
antalya="https://namazvakitleri.diyanet.gov.tr/tr-TR/9225/antalya-icin-namaz-vakti"
artvin="https://namazvakitleri.diyanet.gov.tr/tr-TR/9246/artvin-icin-namaz-vakti"
aydın="https://namazvakitleri.diyanet.gov.tr/tr-TR/9252/aydin-icin-namaz-vakti"
balıkesir="https://namazvakitleri.diyanet.gov.tr/tr-TR/9270/balikesir-icin-namaz-vakti"
bartın="https://namazvakitleri.diyanet.gov.tr/tr-TR/9285/bartin-icin-namaz-vakti"
batman="https://namazvakitleri.diyanet.gov.tr/tr-TR/9288/batman-icin-namaz-vakti"
bayburt="https://namazvakitleri.diyanet.gov.tr/tr-TR/9295/bayburt-icin-namaz-vakti"
bilecik="https://namazvakitleri.diyanet.gov.tr/tr-TR/9297/bilecik-icin-namaz-vakti"
bingöl="https://namazvakitleri.diyanet.gov.tr/tr-TR/9303/bingol-icin-namaz-vakti"
bitlis="https://namazvakitleri.diyanet.gov.tr/tr-TR/9311/bitlis-icin-namaz-vakti"
burdur="https://namazvakitleri.diyanet.gov.tr/tr-TR/9327/burdur-icin-namaz-vakti"
çankırı="https://namazvakitleri.diyanet.gov.tr/tr-TR/9359/cankiri-icin-namaz-vakti"
diyarbakır="https://namazvakitleri.diyanet.gov.tr/tr-TR/9402/diyarbakir-icin-namaz-vakti"
düzce="https://namazvakitleri.diyanet.gov.tr/tr-TR/9414/duzce-icin-namaz-vakti"
elaziğ="https://namazvakitleri.diyanet.gov.tr/tr-TR/9432/elazig-icin-namaz-vakti"
erzincan="https://namazvakitleri.diyanet.gov.tr/tr-TR/9440/erzincan-icin-namaz-vakti"
erzurum="https://namazvakitleri.diyanet.gov.tr/tr-TR/9451/erzurum-icin-namaz-vakti"
gaziantep="https://namazvakitleri.diyanet.gov.tr/tr-TR/9479/gaziantep-icin-namaz-vakti"
giresun="https://namazvakitleri.diyanet.gov.tr/tr-TR/9494/giresun-icin-namaz-vakti"
gümüşhane="https://namazvakitleri.diyanet.gov.tr/tr-TR/9501/gumushane-icin-namaz-vakti"
hakkari="https://namazvakitleri.diyanet.gov.tr/tr-TR/9507/hakkari-icin-namaz-vakti"
hatay="https://namazvakitleri.diyanet.gov.tr/tr-TR/20089/hatay-icin-namaz-vakti"
iğdir="https://namazvakitleri.diyanet.gov.tr/tr-TR/9522/igdir-icin-namaz-vakti"
isparta="https://namazvakitleri.diyanet.gov.tr/tr-TR/9528/isparta-icin-namaz-vakti"
izmir="https://namazvakitleri.diyanet.gov.tr/tr-TR/9560/izmir-icin-namaz-vakti"
kahramanmaraş="https://namazvakitleri.diyanet.gov.tr/tr-TR/9577/kahramanmaras-icin-namaz-vakti"
karaman="https://namazvakitleri.diyanet.gov.tr/tr-TR/9587/karaman-icin-namaz-vakti"
kars="https://namazvakitleri.diyanet.gov.tr/tr-TR/9594/kars-icin-namaz-vakti"
kayseri="https://namazvakitleri.diyanet.gov.tr/tr-TR/9620/kayseri-icin-namaz-vakti"
kirikkale="https://namazvakitleri.diyanet.gov.tr/tr-TR/9635/kirikkale-icin-namaz-vakti"
kirklareli="https://namazvakitleri.diyanet.gov.tr/tr-TR/9638/kirklareli-icin-namaz-vakti"
kirşehir="https://namazvakitleri.diyanet.gov.tr/tr-TR/9646/kirsehir-icin-namaz-vakti"
kütahya="https://namazvakitleri.diyanet.gov.tr/tr-TR/9689/kutahya-icin-namaz-vakti"
malatya="https://namazvakitleri.diyanet.gov.tr/tr-TR/9703/malatya-icin-namaz-vakti"
manisa="https://namazvakitleri.diyanet.gov.tr/tr-TR/9716/manisa-icin-namaz-vakti"
mardin="https://namazvakitleri.diyanet.gov.tr/tr-TR/9726/mardin-icin-namaz-vakti"
mersin="https://namazvakitleri.diyanet.gov.tr/tr-TR/9737/mersin-icin-namaz-vakti"
muğla="https://namazvakitleri.diyanet.gov.tr/tr-TR/9747/mugla-icin-namaz-vakti"
muş="https://namazvakitleri.diyanet.gov.tr/tr-TR/9755/mus-icin-namaz-vakti"
nevşehir="https://namazvakitleri.diyanet.gov.tr/tr-TR/9760/nevsehir-icin-namaz-vakti"
niğde="https://namazvakitleri.diyanet.gov.tr/tr-TR/9766/nigde-icin-namaz-vakti"
ordu="https://namazvakitleri.diyanet.gov.tr/tr-TR/9782/ordu-icin-namaz-vakti"
osmaniye="https://namazvakitleri.diyanet.gov.tr/tr-TR/9788/osmaniye-icin-namaz-vakti"
rize="https://namazvakitleri.diyanet.gov.tr/tr-TR/9799/rize-icin-namaz-vakti"
sakarya="https://namazvakitleri.diyanet.gov.tr/tr-TR/9807/sakarya-icin-namaz-vakti"
şanlıurfa="https://namazvakitleri.diyanet.gov.tr/tr-TR/9831/sanliurfa-icin-namaz-vakti"
siirt="https://namazvakitleri.diyanet.gov.tr/tr-TR/9839/siirt-icin-namaz-vakti"
sinop="https://namazvakitleri.diyanet.gov.tr/tr-TR/9847/sinop-icin-namaz-vakti"
şırnak="https://namazvakitleri.diyanet.gov.tr/tr-TR/9854/sirnak-icin-namaz-vakti"
sivas="https://namazvakitleri.diyanet.gov.tr/tr-TR/9868/sivas-icin-namaz-vakti"
tunceli="https://namazvakitleri.diyanet.gov.tr/tr-TR/9914/tunceli-icin-namaz-vakti"
uşak="https://namazvakitleri.diyanet.gov.tr/tr-TR/9919/usak-icin-namaz-vakti"
van="https://namazvakitleri.diyanet.gov.tr/tr-TR/9930/van-icin-namaz-vakti"
yalova="https://namazvakitleri.diyanet.gov.tr/tr-TR/9935/yalova-icin-namaz-vakti"
yozgat="https://namazvakitleri.diyanet.gov.tr/tr-TR/9949/yozgat-icin-namaz-vakti"
zonguldak="https://namazvakitleri.diyanet.gov.tr/tr-TR/9955/zonguldak-icin-namaz-vakti"


sehir="ınputdan gelen"
r = requests.get(tekirdağ, headers=headers)
c = r.content
abc = BeautifulSoup(c, "html.parser")
tables = abc.find_all('div',class_="tpt-cell")
imsakvakti = tables[0].text
kalansüre=abc.find_all('div',class_="remaining-time-holder")

süre=kalansüre[0].text
günesdogma = tables[2].text
OgleVakti = tables[3].text
İkindiVakti = tables[4].text
AksamVakti = tables[5].text
yatsıVakti = tables[6].text
print(yatsıVakti)