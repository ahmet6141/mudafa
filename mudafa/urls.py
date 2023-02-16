"""mudafa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from sayfa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Base, name='home'),
    path('admin/', admin.site.urls),
    path('giris', views.login),
    path('cıkıs', views.cıkıs),
    path('kayıt', views.kayıt),
    path('Haberler/', views.NewsPage, name='news page'),
    path('haberler/<int:haberid>/', views.HaberDetay),
    path('Hakkımızda/', views.Hakkımızda, name='hakkımızda'),
    path('TarihteBugun/', views.tarihteBugun,name='tarihteBugun'),
    path('tarihteBugun/<int:tarih>/', views.tarihdebgnDetay),
    path('sondakika/<int:sonhaberid>/', views.SonDakika),
    path('İslam/', views.İslam),
    path('Teknoloji/', views.Teknoloji),
    path('Ekonomi/', views.Ekonomi),
    path('Gündelik/', views.Gündelik),
    path('OrtaDoğu/', views.Ortadoğu),
    path('Sohbetler/', views.Sohbetler),
    path('Dünya/', views.Dünya),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)