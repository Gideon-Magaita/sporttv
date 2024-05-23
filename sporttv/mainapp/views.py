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
    return render(request,'pages/home.html',context)




def about_info(request):
    about = About.objects.all()
    context={
        'about': about,
    }
    return render(request,'pages/about.html',context)



def gallery(request):
    movies = Gallery.objects.all()
    # Set the number of movies per page
    movies_per_page = 4 
    
    paginator = Paginator(movies, movies_per_page)
    
    page = request.GET.get('page')
    try:
        movie_page = paginator.page(page)
    except PageNotAnInteger:
        movie_page = paginator.page(1)
    except EmptyPage:
        movie_page = paginator.page(paginator.num_pages)
    
    context = {
        'movie_page': movie_page,
    }
    return render(request, 'pages/gallery.html', context)




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
    return render(request,'pages/contact.html',context)
