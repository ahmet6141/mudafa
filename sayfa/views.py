
from sayfa.models import Kullanıcı,KayanHaberler1Enustsol,Haberler,İşHaber,TarihteBugun,KayanHaberler1EnustSag,SonDakikaHBR
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .NamazVakitleri import *
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import urllib3
import lxml


def Base(request):
    # url = "http://123.59.24.94:8093/login"
    # postdata = urllib.parse.urlencode({'userName': '123', 'pwd': '123'})
    # postdata = postdata.encode('utf-8')
    # f = urllib.request.urlopen(url,postdata)
    # games = GameInfo.objects.all().order_by('-dimDate')[0:6]
    # for i in range(0, len(games)):
    #     games[i].content = games[i].content[0:20]
    KayanhbrUstSol = KayanHaberler1Enustsol.objects.all().order_by('-id')[:5]
    KayanhbrUstSag=KayanHaberler1EnustSag.objects.all().order_by('-id')[:5]
    sondakikahbrr=SonDakikaHBR.objects.all().order_by('-Tarih')
    # gamelist = GameInfo.objects.all()[0:3]
    #
    news = Haberler.objects.all()[0:7]
    #news=news[1:7]

    context={'KayanhbrUstSol': KayanhbrUstSol,'news':news,'KayanhbrUstSag':KayanhbrUstSag,'sondakikahbrr':sondakikahbrr}
    return render(request, "index.html",context)
PageCount = 8
PAGERLEN = 8

def login(request):
    if request.method == "POST":
        uf = request.POST
        Kullanıcıadı = uf.get('Kullanıcıadı')
        pwd = uf.get('pwd')
        # d=sign(username+pwd)
        # data = {'userName': username, 'pwd': pwd, 'sign': d}
        # callbackData = {}#返回数据
        # callbackData = json.loads(
        #     str(post('http://123.59.24.94:8093/login', data), encoding="utf-8"))
        # if(callbackData['code'] == 1):
        #     request.session['username'] = username
        #     return HttpResponseRedirect('/')
        if Kullanıcı.objects.filter(Kullanıcı_adı=Kullanıcıadı,parola=pwd):
            request.session['Kullanıcı_adı']=Kullanıcıadı
            return  HttpResponseRedirect('/')
        else:
            return render(request, 'giris.html',{'info':'1'})

    else:
        if('Kullanıcı_adı' not in request.session):
            return render(request, 'giris.html')
        else:
            return HttpResponseRedirect('/')

def İslam(request):
    hbr=Haberler.objects.filter(HaberTur="İslam")
    context={'hbr':hbr};
    return render(request,'hbrsayfaları/İslamihbr.html',context)
def Ekonomi(request):
    hbr=Haberler.objects.filter(HaberTur="Ekonomi")
    context={'hbr':hbr};
    return render(request,'hbrsayfaları/Ekonomihbr.html',context)
def Gündelik(request):
    hbr = Haberler.objects.filter(HaberTur="Gündelik")
    context = {'hbr': hbr};
    return render(request,'hbrsayfaları/Gündelikhbr.html',context)
def Ortadoğu(request):
    hbr = Haberler.objects.filter(HaberTur="OrtaDoğu")
    context = {'hbr': hbr};
    return render(request,'hbrsayfaları/Ortadoğuhbr.html',context)
def Teknoloji(request):
    hbr = Haberler.objects.filter(HaberTur="teknoloji")
    context = {'hbr': hbr};
    return render(request,'hbrsayfaları/Teknolojihbr.html',context)
def Dünya(request):
    hbr = Haberler.objects.filter(HaberTur="Dünya")
    context = {'hbr': hbr};
    return render(request,'hbrsayfaları/DünyaHbr.html',context)
def Sohbetler(request):
    hbr = Haberler.objects.filter(HaberTur="Sohbetler")
    context = {'hbr': hbr};
    return render(request,'hbrsayfaları/Sohbetler.html',context)
def cıkıs(request):
    del request.session['Kullanıcı_adı']
    return HttpResponseRedirect('/')

def namazvakti(request):
    sehir = "ınputdan gelen"
    r = requests.get(istanbul, headers=headers)
    c = r.content
    abc = BeautifulSoup(c, "html.parser")
    tables = abc.find_all('div', class_="tpt-cell")
    imsakvakti = tables[0].text
    günesdogma = tables[2].text
    OgleVakti = tables[3].text
    İkindiVakti = tables[4].text
    AksamVakti = tables[5].text
    yatsıVakti = tables[6].text
    kalansüre = abc.find_all('div', class_="remaining-time-holder")
    context = {'imsakvakti': imsakvakti, 'kalansüre': kalansüre,'sehir':sehir,'günesdogma':günesdogma,'OgleVakti':OgleVakti,'İkindiVakti':İkindiVakti,'AksamVakti':AksamVakti,'yatsıVakti':yatsıVakti}
    return render(request,context)
def tarihteBugun(request):
    try:
        curpage = int(request.GET.get('curpage', '1'))
        allpage = int(request.GET.get('allpage', '1'))
        pagetype = str(request.GET.get('pagetype', ''))
    except ValueError:
        curpage = 1
        allpage = 1
        pagetype = 1
    if pagetype == 'pagedown':
        curpage += 1
    elif pagetype == 'pageup':
        curpage -= 1
    elif pagetype == 'pageto':
        pass
    startpos = (curpage - 1) * PageCount
    endpos = startpos + PageCount
    tarihtbugn = TarihteBugun.objects.all().order_by('-Yayıntarih')[startpos:endpos]
    if curpage == 1 and allpage == 1:
        Butunyayındakiler = TarihteBugun.objects.count()
        allpage = Butunyayındakiler // PageCount
        remainPost = Butunyayındakiler % PageCount
        if remainPost > 0:
            allpage += 1
    pagelist = []  # below are the logic of pagination
    if(allpage - curpage > PAGERLEN - 2):
        for i in range(curpage - 1 - PAGERLEN // 2 if curpage - 1 - PAGERLEN // 2 > 0 else 0, curpage - 1 + PAGERLEN // 2):
            pagelist.append(i + 1)
            if len(pagelist) > PAGERLEN - 1:
                break
    else:
        if (curpage - 1 - PAGERLEN // 2 > 0):
            for i in range(curpage - 1 - PAGERLEN // 2, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break
        else:
            for i in range(0, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break
    context = {'tarihtbugn': tarihtbugn,'allpage': allpage, 'borderpage': allpage - 3, 'pagelist': pagelist, 'curpage': curpage}
    return render(request, "tarihtebgn.html", context)

def tarihdebgnDetay(request,tarih):
    yayindakiler=TarihteBugun.objects.get(id=tarih)
    context={'yayindakiler':yayindakiler}
    return render(request,"TarihdeBugünDetay.html", context)
def kayıt(request):
    if request.method == "POST":
        try:
            kullanıcı_adıı = request.POST.get('username', None)
            parola = request.POST.get('psd', None)
            email = request.POST.get('mail',None)
            if Kullanıcı.objects.filter(Kullanıcı_adı=kullanıcı_adıı):
                return HttpResponse('Kullanıcı Adı Var')
            else:
                user=Kullanıcı()
                user.Kullanıcı_adı=kullanıcı_adıı
                user.parola=parola
                user.mail=email
                user.save()
                request.session['kullanıcı_adı']=kullanıcı_adıı
                return HttpResponseRedirect('/giris')
        except:
            pass
    return render(request, 'kayıt.html')

BPageCount = 3
BPAGERLEN = 8
def NewsPage(request):
    try:
        curpage = int(request.GET.get('curpage', '1'))
        allpage = int(request.GET.get('allpage', '1'))
        pagetype = str(request.GET.get('pagetype', ''))
    except ValueError:
        curpage = 1
        allpage = 1
        pagetype = 1
    if pagetype == 'pagedown':
        curpage += 1
    elif pagetype == 'pageup':
        curpage -= 1
    elif pagetype == 'pageto':
        pass
    startpos = (curpage - 1) * PageCount
    endpos = startpos + PageCount
    posts = Haberler.objects.all().order_by('-dimDate')[startpos:endpos]
    if curpage == 1 and allpage == 1:
        allNewsCount = Haberler.objects.count()
        allpage = allNewsCount // PageCount
        remainPost = allNewsCount % PageCount
        if remainPost > 0:
            allpage += 1
    pagelist = []  # below are the logic of pagination
    if(allpage - curpage > PAGERLEN - 2):
        for i in range(curpage - 1 - PAGERLEN // 2 if curpage - 1 - PAGERLEN // 2 > 0 else 0, curpage - 1 + PAGERLEN // 2):
            pagelist.append(i + 1)
            if len(pagelist) > PAGERLEN - 1:
                break
    else:
        if (curpage - 1 - PAGERLEN // 2 > 0):
            for i in range(curpage - 1 - PAGERLEN // 2, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break
        else:
            for i in range(0, curpage - 1 + PAGERLEN // 2 if curpage - 1 + PAGERLEN // 2 < allpage else allpage):
                pagelist.append(i + 1)
                if len(pagelist) > PAGERLEN - 1:
                    break

    return render(request, 'haberler.html', {'news': posts, 'allpage': allpage, 'borderpage': allpage - 3, 'pagelist': pagelist, 'curpage': curpage})
def HaberDetay(request, haberid):
    Haberlr = Haberler.objects.get(id=haberid)
    return render(request, 'haberdetay.html', locals())
def Hakkımızda(request):
    return render(request, "hakkımızda.html")
def SonDakika(request,sonhaberid):
    HaberSayfası= SonDakikaHBR.objects.get(id=sonhaberid)
    context = {'HaberSayfası': HaberSayfası}
    return render(request, 'SondakikaHaberSayfa.html', context)