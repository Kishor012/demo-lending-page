from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Advertise, Makemoney, Technology
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    ads_all_post = Advertise.objects.all()[0:2]
    tech_all_post = Technology.objects.all()[0:1]
    make_all_post = Makemoney.objects.all()[0:2]
    tech_posts = Technology.objects.get(pk=1)
    make_posts = Makemoney.objects.get(pk=2)
    return render(request, 'blogpost/home.html', {
        'ads_all_post': ads_all_post, 
        'tech_all_post': tech_all_post, 
        'make_all_post': make_all_post, 
        'tech_posts': tech_posts,
        'make_posts': make_posts
        })

def advertise(request):
    advertise_post = Advertise.objects.all().order_by('id')
    for post in advertise_post:
        desc_post = post.desc[0:150]

    paginator = Paginator(advertise_post, 10, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    return render(request, 'blogpost/advertise.html', {'desc_post': desc_post, 'page_obj': page_obj })     

def technology(request):
    technology_post = Technology.objects.all().order_by('id')
    for post in technology_post:
        desc_post = post.desc[0:150]

    paginator = Paginator(technology_post, 10, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    
    return render(request, 'blogpost/technology.html', {
        'technology_post': technology_post,
         'desc_post': desc_post,
         'page_obj':page_obj
         })    


def make_money(request):
    makemoney_post = Makemoney.objects.all().order_by('id')
    for post in makemoney_post:
        desc_post = post.desc[0:150]

    paginator = Paginator(makemoney_post, 10, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogpost/make-money.html', {
        'makemoney_post': makemoney_post,
        'desc_post': desc_post,
        'page_obj': page_obj
         }) 


def ads_desc(request, id):
    pi = Advertise.objects.get(pk=id)
    return render(request, 'blogpost/ads-desc.html',{'pi':pi}) 

def tech_desc(request, id):
    pi = Technology.objects.get(pk=id)
    return render(request, 'blogpost/tech-desc.html',{'pi':pi})

def make_desc(request, id):
    pi = Makemoney.objects.get(pk=id)
    return render(request, 'blogpost/make-desc.html', {'pi':pi})    
