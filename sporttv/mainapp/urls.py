from django.urls import path
from .import views
from .import admins
urlpatterns=[
    path('',views.home,name='home'),
    path('about_info',views.about_info,name='about_info'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('more_news/<int:id>',views.more_news,name='more_news'),
    #adminurls
    path('admin_home',admins.admin_home,name='admin_home'),
    path('slider_page',admins.slider_page,name='slider_page'),
    path('edit_slider/<int:id>',admins.edit_slider,name='edit_slider'),
    path('delete_slider/<int:id>',admins.delete_slider,name='delete_slider'),
    path('news_details',admins.news_details,name='news_details'),
    path('edit_news_details/<int:id>',admins.edit_news_details,name='edit_news_details'),
    path('delete_news/<int:id>',admins.delete_news,name='delete_news'),
    path('gallery_details',admins.gallery_details,name='gallery_details'),
    path('edit_gallery/<int:id>',admins.edit_gallery,name='edit_gallery'),
    path('delete_gallery/<int:id>',admins.delete_gallery,name='delete_gallery'),
    path('about_details',admins.about_details,name='about_details'),
    path('edit_about_details/<int:id>',admins.edit_about_details,name='edit_about_details'),
    path('delete_about_details/<int:id>',admins.delete_about_details,name='delete_about_details'),
    path('contact_details',admins.contact_details,name='contact_details'),
    path('delete_contact/<int:id>',admins.delete_contact,name='delete_contact'),
    path('email_details',admins.email_details,name='email_details'),
    path('delete_email/<int:id>',admins.delete_email,name='delete_email'),
    #authenticationurls
    path('login_user', admins.login_user,name='login_user'),
    path('logoutUser', admins.logoutUser,name='logoutUser'),

]