from django.contrib import admin
from .models import Advertise, Makemoney, Technology
# Register your models here.

@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date', 'website', 'webname', 'desc',
                    'subtitleone','subphotoone','subdescone',
                    'subtitletwo', 'subphototwo', 'subdesctwo',
                    'subtitlethree', 'subphotothree', 'subdescthree'
                    ] 
@admin.register(Makemoney)
class MakemoneyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date', 'desc',
                    'subtitleone','subphotoone','subdescone',
                    'subtitletwo', 'subphototwo', 'subdesctwo',
                    'subtitlethree', 'subphotothree', 'subdescthree'
                    ] 

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date', 'desc',
                    'subtitleone','subphotoone','subdescone',
                    'subtitletwo', 'subphototwo', 'subdesctwo',
                    'subtitlethree', 'subphotothree', 'subdescthree'
                    ]   

