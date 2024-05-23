from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *


def admin_home(request):
    slider = Slider.objects.all().count()
    news = News.objects.all().count()
    gallery = Gallery.objects.all().count()
    context={
        'gallery': gallery,
        'slider': slider,
        'news': news,
    }
    return render(request, 'pages/admins/home.html',context)

def slider_page(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        form = SliderForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'slider saved successfully')
            return redirect('slider_page')
        else:
            messages.error(request,'something went wrong')
            return redirect('slider_page')
    else:
        form = SliderForm()
    context={
        'form': form,
        'slider': slider,
    }
    return render(request, 'pages/admins/slider.html',context)


def edit_slider(request,id):
    slider = Slider.objects.get(id=id)
    form = SliderForm(request.POST or None,request.FILES or None,instance=slider)
    if form.is_valid():
        form.save()
        messages.success(request,'slider updated successfully')
        return redirect('slider_page')
    context={
        'form':form,
    }
    return render(request, 'pages/admins/edit-slider.html',context)


def delete_slider(request,id):
    slider = Slider.objects.get(id=id)
    slider.delete()
    messages.success(request,'slider deleted successfully')
    return redirect('slider_page')


def news_details(request):
    news = News.objects.all()
    if request.method=='POST':
        form = NewsForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'news saved successfully')
            return redirect('news_details')
        else:
            messages.error(request,'something went wrong')
            return redirect('news_details')
    else:
        form = NewsForm()
    context={
        'form': form,
        'news':news,
    }
    return render(request,'pages/admins/news.html',context)


def edit_news_details(request,id):
    news = News.objects.get(id=id)
    form = NewsForm(request.POST or None,instance=news)
    if form.is_valid():
        form.save()
        messages.success(request,'news updated successfully')
        return redirect('news_details')
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-news.html',context)


def delete_news(request,id):
    news = News.objects.get(id=id)
    news.delete()
    messages.success(request,'news deleted successfully')
    return redirect('news_details')


def gallery_details(request):
    gall = Gallery.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'gallery details saved successfully')
            return redirect('gallery_details')
        else:
            messages.error(request,'Something went wrong')
            return redirect('gallery_details')
    else:
        form = GalleryForm()
    context={
        'form':form,
        'gall':gall,
    }
    return render(request,'pages/admins/gallery.html',context)


def edit_gallery(request,id):
    gall = Gallery.objects.get(id=id)
    form = GalleryForm(request.POST or None,request.FILES or None,instance=gall)
    if form.is_valid():
        form.save()
        messages.success(request,'gallery details updated')
        return redirect('gallery_details')
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-gallery.html',context)


def delete_gallery(request,id):
    gall = Gallery.objects.get(id=id)
    gall.delete()
    messages.success(request,'details deleted!')
    return redirect('gallery_details')

def about_details(request):
    about = About.objects.all()
    if request.method == 'POST':
        form = AboutForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'about info added successfully')
            return redirect('about_details')
        else:
            messages.info(request,'about info deleted')
            return redirect('about_details')
    else:
        form = AboutForm()
    context={
        'form':form,
        'about':about,
    }
    return render(request,'pages/admins/about.html',context)


def edit_about_details(request,id):
    about = About.objects.get(id=id)
    form = AboutForm(request.POST or None,request.FILES or None,instance=about)
    if form.is_valid():
        form.save()
        messages.success(request,'about details updated')
        return redirect('about_details')
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-about.html',context)


def delete_about_details(request,id):
    about = About.objects.get(id=id)
    about.delete()
    messages.success(request,'details deleted!')
    return redirect('about_details')


def contact_details(request):
    contact = Contact.objects.all()
    context={
        'contact':contact,
    }
    return render(request,'pages/admins/contact.html',context)

def delete_contact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request,'details deleted!')
    return redirect('contact_details')

def email_details(request):
    email = Email.objects.all()
    context={
        'email':email,
    }
    return render(request,'pages/admins/emails.html',context)

def delete_email(request,id):
    email = Email.objects.get(id=id)
    email.delete()
    messages.success(request,'details deleted!')
    return redirect('email_details')