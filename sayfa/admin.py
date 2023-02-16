from django.contrib import admin
from sayfa.models import Haberler,Kullanıcı,KayanHaberler1Enustsol,İşHaber,TarihteBugun,KayanHaberler1EnustSag,SonDakikaHBR

class HaberAdmin(admin.ModelAdmin):

    class Media:
        js = (

            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',

        )
admin.site.register(Haberler,HaberAdmin)
admin.site.register(Kullanıcı)
admin.site.register(İşHaber, HaberAdmin)
admin.site.register(KayanHaberler1Enustsol)
admin.site.register(TarihteBugun)
admin.site.register(KayanHaberler1EnustSag)
admin.site.register(SonDakikaHBR)