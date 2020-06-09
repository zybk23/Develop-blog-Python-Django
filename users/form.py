from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    username=forms.CharField(label="Kullanıcı Adı")
    email=forms.EmailField(max_length=50,label="E-mail")
    password1=forms.CharField(label="Parola",widget=forms.PasswordInput)
    password2=forms.CharField(label="Parola tekrar",widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model=User
        fields=("username","email","password1","password2")

class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super (UserProfileForm,self).__init__(*args,**kwargs)

        self.helper=FormHelper()
        self.helper.form_method="post"
        self.helper.field_class='mt-10'
        self.helper.layout=Layout(
            Field("birth_day",css_class="single-input"),
            Field("bio",css_class="single-input"),
            Field("image",css_class="single-input"),
            
        )
        self.helper.add_input(Submit("submit","Update",css_class="genric-btn success-border medium"))
    class Meta:
        model=UserProfile
        fields=('birth_day',"bio","image")
        widgets={
            'birth_day':forms.DateInput(attrs={"type":"date"})
        }    
