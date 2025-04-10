from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(
        label="Телефон",
        required=False,
        max_length=20,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '79123456789'
        })
    )
    adress = forms.CharField(
        label="Адрес",
        required=False,
        max_length=256,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'г. Москва, ул. Примерная, д.1'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'adress', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CustomUserChangeForm(UserChangeForm):
    password = None  # Убираем поле смены пароля

    phone = forms.CharField(
        label="Телефон",
        required=False,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    adress = forms.CharField(
        label="Адрес",
        required=False,
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'adress')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }