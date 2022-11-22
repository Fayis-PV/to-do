from django import forms
from django.forms import ModelForm
from .models import ToDoProject
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ToDoProjectForm(forms.ModelForm):
    class Meta:
        model = ToDoProject
        fields = '__all__'
        template_name = 'form_snippet.html'
        labels = {
            'project_name':'',
            'deadline': '',
            'timeline': '',
        }
        widgets = {
            'project_name': forms.TextInput(attrs={'class':'col-md-12 form-control m-2 name','placeholder':'To Do...'}),
            'deadline': forms.DateTimeInput(attrs={'class':'col-md-12 form-control date','placeholder':'Select A Deadline','type':'date'}),
            'timeline': forms.TimeInput(attrs={'class':'col-md-12 form-control time','placeholder':'Select A Deadline','type':'time'})
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'username':'',
            'email':'',
            'password1':'Password :',
            'password2': 'Confirm Password :',
        }
        widgets ={
            'username': forms.TextInput(attrs={'class':'col-md-12 form-control m-2','placeholder':'Enter Name...'}),
            'email': forms.TextInput(attrs={'class':'col-md-12 form-control m-2','placeholder':'Enter Email...'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control m-2 col-md-12','placeholder':'Enter a password'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control m-2 col-md-12','placeholder':'Confirm password'}),
        }

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields= [
#             'username',
#             'email',
#             'phone_number',
#             'password'
#         ]
        
#         labels = {
#             'username':'',
#             'email':'',
#             'phone_number':'',
#             'password': '',
#         }
#         widgets ={
#             'username': forms.TextInput(attrs={'class':'col-md-12 form-control m-2','placeholder':'Enter Name...'}),
#             'email': forms.TextInput(attrs={'class':'col-md-12 form-control m-2','placeholder':'Enter Email...'}),
#             'phone_number': forms.TextInput(attrs={'class':'col-md-12 form-control m-2','placeholder':'Enter Phone Number...'}),
#             'password': forms.PasswordInput(attrs={'class':'form-control m-2 col-md-12','placeholder':'Enter a password'})
#         }



class LoginForm(forms.Form):
    your_name = forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={'class':'form-control col-md-12 m-2','placeholder':'Enter Name...'}))
    your_password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control col-md-12 m-2','placeholder':'Enter password...'}))
