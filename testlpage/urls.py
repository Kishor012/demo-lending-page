from unicodedata import name
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve
from blogpost import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='back_home'),
    path('ads/', views.advertise, name='back_ads'),
    path('tech/', views.technology, name='back_tech'),
    path('make/', views.make_money, name='back_make'),
    path('ades/<int:id>/', views.ads_desc, name='ads-desc'),
    path('tdes/<int:id>/', views.tech_desc, name='tech-desc'),
    path('mdes/<int:id>/', views.make_desc, name='make-desc'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
"""
