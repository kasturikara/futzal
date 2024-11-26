from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('about/', views.about, name='about'),
    
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/list/', views.admin_list_view, name='admin_list'),
    path('admin/tambah/', views.admin_create_view, name='admin_create'),
    
    path('lapangan/', views.LapanganListView.as_view(), name='lapangan_list'),
    path('lapangan/tambah/', views.LapanganCreateView.as_view(), name='lapangan_create'),
    path('lapangan/<int:pk>/update/', views.LapanganUpdateView.as_view(), name='lapangan_update'),
    path('lapangan/<int:pk>/delete/', views.LapanganDeleteView.as_view(), name='lapangan_delete'),
]

