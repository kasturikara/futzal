from django import forms
from .models import Lapangan

class LapanganCreateForm(forms.ModelForm):
    class Meta:
        model = Lapangan
        fields = ('nama', 'deskripsi', 'harga', 'status')

class LapanganUpdateForm(forms.ModelForm):
    class Meta:
        model = Lapangan
        fields = ('nama', 'deskripsi', 'harga', 'status')

class LapanganDeleteForm(forms.ModelForm):
    class Meta:
        model = Lapangan
        fields = ()