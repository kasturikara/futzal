from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Lapangan, Staff, Admin
from .forms import *


class LandingPageView(TemplateView):
    template_name = "public/landing.html"
    

def about(request):
    return render(request, 'public/about.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Register berhasil')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Selamat datang, ' + user.username)
                
                # redirect berdasarkan role
                if hasattr(user, 'profile'):
                    return redirect(reverse('landing'))
                # elif hasattr(user, 'staff'):
                    # return redirect(reverse('staff'))
                elif hasattr(user, 'admin'):
                    return redirect(reverse('admin_dashboard'))
                else:
                    return redirect(reverse('landing'))
            else:
                messages.error(request, 'Username atau password salah')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('landing'))


class LapanganListView(LoginRequiredMixin, ListView):
    model = Lapangan
    template_name = 'admin/lapangan_list.html'
    context_object_name = 'lapangan_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Anda harus login terlebih dahulu untuk melihat lapangan!')
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)


class LapanganCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Lapangan
    form_class = LapanganCreateForm
    template_name = 'admin/lapangan_create.html'
    success_url = reverse_lazy('lapangan_list')
    permission_required = 'admin.manage_lapangan'

    def form_valid(self, form):
        messages.success(self.request, 'Lapangan berhasil ditambahkan')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Anda harus login sebagai admin terlebih dahulu untuk menambahkan lapangan!')
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class LapanganUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Lapangan
    form_class = LapanganUpdateForm
    template_name = 'admin/lapangan_update.html'
    success_url = reverse_lazy('lapangan_list')
    permission_required = 'admin.manage_lapangan'

    def form_valid(self, form):
        if 'foto_lapangan' in self.request.FILES:
            self.object.foto_lapangan = self.request.FILES['foto_lapangan']
        messages.success(self.request, 'Lapangan berhasil diperbarui')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Anda harus login sebagai admin terlebih dahulu untuk mengubah lapangan!')
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class LapanganDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Lapangan
    form_class = LapanganDeleteForm
    template_name = 'admin/lapangan_delete.html'
    success_url = reverse_lazy('lapangan_list')
    permission_required = 'admin.manage_lapangan'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Lapangan berhasil dihapus')
        return super().delete(request, *args, **kwargs)


@login_required(login_url='login')
@permission_required('admin.manage_users', login_url='login')
def admin_dashboard(request):
    return render(request, 'admin/index.html')

@login_required(login_url='login')
@permission_required('admin.manage_users', login_url='login')
def admin_list_view(request):
    admins = Admin.objects.all()
    context = {
        'admins': admins,
    }
    return render(request, 'admin/admin_list.html', context)

def admin_create_view(request):
    if request.method == 'POST':
        form = AdminCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin berhasil ditambahkan')
            return redirect(reverse('admin_list'))
    else:
        form = AdminCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'admin/admin_create.html', context)

# class AdminUpdateView(UpdateView):
#     model = Admin
#     fields = ('nama', 'deskripsi', 'harga')
#     template_name = 'admin_form.html'
#     success_url = '/admin/'

# class AdminDeleteView(DeleteView):
#     model = Admin
#     template_name = 'admin_confirm_delete.html'
#     success_url = '/admin/'


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