from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    slider = Slider.objects.all()
    news = News.objects.filter(status='publish')
    gall = Gallery.objects.filter(status='publish')
    if request.method == 'POST':
        form = EmailForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Subscribed successfully')
            return redirect('home')
        else:
            messages.error(request,'something went wrong')
            return redirect('home')
    else:
        form = EmailForm()
    context = {
        'slider': slider,
        'news': news,
        'form': form,
        'gall':gall,
    }
    return render(request,'pages/users/home.html',context)




def more_news(request,id):
    news = News.objects.get(id=id)
    context={
        'news': news
    }
    return render(request,'pages/users/news.html',context)



def about_info(request):
    about = About.objects.all()
    context={
        'about': about,
    }
    return render(request,'pages/users/about.html',context)




def gallery(request):
    category = request.GET.get('category', 'movie')  # Default to 'movie' if no category is specified
    movies = Gallery.objects.filter(category=category)

    # Set the number of movies per page
    movies_per_page = 5 
    
    paginator = Paginator(movies, movies_per_page)
    
    page = request.GET.get('page')
    try:
        movie_page = paginator.page(page)
    except PageNotAnInteger:
        movie_page = paginator.page(1)
    except EmptyPage:
        movie_page = paginator.page(paginator.num_pages)
    
    #for cartoon
    category = request.GET.get('category','cartoon')  # Default to 'movie' if no category is specified
    cartoon = Gallery.objects.filter(category=category)
    # Set the number of movies per page
    catoon_per_page = 5 
    
    paginator = Paginator(cartoon, catoon_per_page)
    
    page = request.GET.get('page')
    try:
        cartoon_page = paginator.page(page)
    except PageNotAnInteger:
        cartoon_page = paginator.page(1)
    except EmptyPage:
        cartoon_page = paginator.page(paginator.num_pages)

    #for sports
    category = request.GET.get('category','sports')  # Default to 'movie' if no category is specified
    sports = Gallery.objects.filter(category=category)
    # Set the number of movies per page
    catoon_per_page = 5 
    
    paginator = Paginator(sports, catoon_per_page)
    
    page = request.GET.get('page')
    try:
        sports_page = paginator.page(page)
    except PageNotAnInteger:
        sports_page = paginator.page(1)
    except EmptyPage:
        sports_page = paginator.page(paginator.num_pages)
    
    context = {
        'movie_page': movie_page,
        'cartoon_page':cartoon_page,
        'sports_page':sports_page,
    }
    return render(request, 'pages/users/gallery.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Message sent successfully')
            return redirect('contact')
        else:
            messages.error(request,'something went wrong')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request,'pages/users/contact.html',context)
