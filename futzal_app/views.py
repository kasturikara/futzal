from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Lapangan, Staff, Admin
from .forms import LapanganCreateForm, LapanganUpdateForm, LapanganDeleteForm


# def admin_dashboard(request):
#     return render(request, 'admin/index.html')


class LandingPageView(TemplateView):
    template_name = "public/landing.html"
    

class LapanganListView(ListView):
    model = Lapangan
    template_name = 'admin/lapangan_list.html'

    
class LapanganCreateView(CreateView):
    model = Lapangan
    form_class = LapanganCreateForm
    template_name = 'admin/lapangan_create.html'
    success_url = '/lapangan/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class LapanganUpdateView(UpdateView):
    model = Lapangan
    form_class = LapanganUpdateForm
    template_name = 'admin/lapangan_update.html'

    def get_success_url(self):
        return reverse('lapangan_list')
    
    def form_valid(self, form):
        if 'foto_lapangan' in self.request.FILES:
            self.object.foto_lapangan = self.request.FILES['foto_lapangan']
        return super().form_valid(form)

class LapanganDeleteView(DeleteView):
    model = Lapangan
    form_class = LapanganDeleteForm
    template_name = 'admin/lapangan_confirm_delete.html'
    success_url = '/lapangan/'

# class StaffListView(ListView):
#     model = Staff
#     template_name = 'staff_list.html'

# class StaffCreateView(CreateView):
#     model = Staff
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'staff_form.html'
#     success_url = '/staff/'

# class StaffUpdateView(UpdateView):
#     model = Staff
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'staff_form.html'
#     success_url = '/staff/'

# class StaffDeleteView(DeleteView):
#     model = Staff
#     template_name = 'staff_confirm_delete.html'
#     success_url = '/staff/'

# class AdminListView(ListView):
#     model = Admin
#     template_name = 'admin_list.html'

# class AdminCreateView(CreateView):
#     model = Admin
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'admin_form.html'
#     success_url = '/admin/'

# class AdminUpdateView(UpdateView):
#     model = Admin
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'admin_form.html'
#     success_url = '/admin/'

# class AdminDeleteView(DeleteView):
#     model = Admin
#     template_name = 'admin_confirm_delete.html'
#     success_url = '/admin/'

# class UserListView(ListView):
#     model = User
#     template_name = 'user_list.html'

# class UserCreateView(CreateView):
#     model = User
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'user_form.html'
#     success_url = '/user/'

# class UserUpdateView(UpdateView):
#     model = User
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'user_form.html'
#     success_url = '/user/'

# class UserDeleteView(DeleteView):
#     model = User
#     template_name = 'user_confirm_delete.html'
#     success_url = '/user/'    