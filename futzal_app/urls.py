from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    
    path('lapangan/', views.LapanganListView.as_view(), name='lapangan_list'),
    path('lapangan/tambah/', views.LapanganCreateView.as_view(), name='lapangan_create'),
    path('lapangan/<int:pk>/update/', views.LapanganUpdateView.as_view(), name='lapangan_update'),
    path('lapangan/<int:pk>/delete/', views.LapanganDeleteView.as_view(), name='lapangan_delete'),
]
