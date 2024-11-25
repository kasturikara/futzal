from django.db import models
from django.contrib.auth.models import User

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
        
    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    
    
class Lapangan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('tersedia', 'Tersedia'), ('tidak_tersedia', 'Tidak Tersedia')], default='tersedia')
    
    def __str__(self):
        return self.nama
    
    
class Pemesanan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('diproses', 'Diproses'), ('selesai', 'Selesai')], default='pending')
    
    def __str__(self):
        return f"Pemesanan {self.id} - {self.user.username}"