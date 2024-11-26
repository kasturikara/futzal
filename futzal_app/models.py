from django.db import models
from django.contrib.auth.models import User

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)
    foto_profil = models.ImageField(upload_to='profile/user/', blank=True, null=True)
    
    class Meta:
        permissions = [
            ("view_own_profile", "Can view own profile"),
            ("edit_own_profile", "Can edit own profile"),
            ("make_pemesanan", "Can make pemesanan"),
        ]

    def __str__(self):
        return self.nama
        
    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)
    foto_profil = models.ImageField(upload_to='profile/staff/', blank=True, null=True)

    class Meta:
        permissions = [
            ("view_staff_dashboard", "Can view staff dashboard"),
            ("manage_pemesanan", "Can manage pemesanan"),
            ("update_pemesanan", "Can update pemesanan"),
        ]

    def __str__(self):
        return self.nama

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)
    foto_profil = models.ImageField(upload_to='profile/admin/', blank=True, null=True)

    class Meta:
        permissions = [
            ("manage_users", "Can manage users"),
            ("manage_lapangan", "Can manage lapangan"),
            ("manage_pemesanan", "Can manage pemesanan"),
        ]

    def __str__(self):
        return self.nama
    
    
class Lapangan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('tersedia', 'Tersedia'), ('tidak_tersedia', 'Tidak Tersedia')], default='tersedia')
    foto_lapangan = models.ImageField(upload_to='lapangan/', blank=True, null=True)
    
    def __str__(self):
        
        return self.nama
    
    
class Pemesanan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('diproses', 'Diproses'), ('selesai', 'Selesai')], default='pending')
    
    def __str__(self):
        return f"{self.staff} - {self.profile} - {self.lapangan} - {self.tanggal} - {self.waktu_mulai} - {self.waktu_selesai}"