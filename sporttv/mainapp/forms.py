from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from ckeditor.widgets import CKEditorWidget
#auth imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


#add user form
class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'enter Password'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))




class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email_title']




class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'



class SliderForm(ModelForm):      
    class Meta:
        model = Slider
        fields = ['image','title','sub_title']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': 'required'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'required': 'required'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sub-title', 'required': 'required'}),
        }


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields=['description']

        widgets={
            'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter about info', 'required': 'required'}),
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields=['news_title','description','status']

        widgets={
            'news_title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter news title', 'required': 'required'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter description','required': 'required'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields=['title','image','category','status']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter  title', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': 'required'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = ['description']
        widgets = {
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about info','required':'required'}),
        }