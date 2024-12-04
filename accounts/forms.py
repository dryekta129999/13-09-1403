from django import forms
from django.contrib.auth.models import User
from .models import *

error = {
    'min_length' : 'حداقل می بایست 5 کاراکتر باشد',
    'required' : 'این فیلد اجباری است',
}

class UserRegisterForm(forms.Form):
    user_name = (
        forms.CharField(max_length=50 ,
    widget=forms.TextInput(attrs={'placeholder' : 'نام کاربری خود را وارد نمایید'}) ,  error_messages=error) )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'email....'}) , error_messages=error)
    first_name = forms.CharField(max_length=10 , min_length=5 , error_messages=error)
    last_name = forms.CharField(max_length=100 , error_messages=error)
    password_1 = (
        forms.CharField(max_length=100 ,
                        widget=forms.PasswordInput(attrs={'placeholder' : 'پسورد ...'})))
    password_2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder' : 'تکرار پسورد ...'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username = user).exists():
            raise forms.ValidationError('نام کاربری تکرای است')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('ایمیل تکراری است')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2 :
            raise forms.ValidationError('Password not match')
        elif len(password2) < 8 :
            raise forms.ValidationError('پسورد می بایست حداقل 8 کارکتر باشد')
        elif not any(x.isupper() for x in password2):
            raise forms.ValidationError('پسورد می بایست شامل حداقل یک حرف بزرگ باشد')
        return password2


class UserLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

class UserUpdateForm(forms.ModelForm) :
    class Meta:
        model = User
        fields = ['email' , 'first_name' , 'last_name']

class ProfileUpdateForm(forms.ModelForm) :
    class Meta:
        model = Profile
        fields = ['phone' , 'address' , 'profile_image']
