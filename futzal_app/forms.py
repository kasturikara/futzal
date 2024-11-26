from django import forms
from .models import Lapangan

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