from django import forms
from django.contrib.auth.models import User
 

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите свой email', }), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', }), label='')
    # (label='Введите свой email')

    def clean(self):
        self.cleaned_data.get('username')
        self.cleaned_data.get('password')
        return self.cleaned_data

class RegistrationForm(forms.ModelForm):
    email =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите свой email', }), label='')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', }), label='')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно', }), label='')
    class Meta:
        model = User 
        fields = ('email',)

    def clean_password2(self):
        cd = self.cleaned_data 
        if cd ['password1'] != ['password2']:
            raise forms.ValidationError('Ваши пароли не совпали')
        return cd['password2']
