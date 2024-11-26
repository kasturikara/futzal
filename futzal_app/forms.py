from django import forms
from django.contrib.auth.models import User
from .models import Lapangan, Admin


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class LapanganCreateForm(forms.ModelForm):
    class Meta:
        model = Lapangan
        fields = ('nama', 'deskripsi', 'harga', 'status', 'foto_lapangan')

class LapanganUpdateForm(forms.ModelForm):
    class Meta:
        model = Lapangan
        fields = ('nama', 'deskripsi', 'harga', 'status', 'foto_lapangan')

class LapanganDeleteForm(forms.ModelForm):
    class Meta:
        model = Lapangan
        fields = ()
        
        
class AdminCreateForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('user', 'nama', 'no_telepon', 'foto_profil')
