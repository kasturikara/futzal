from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if not request.path.startswith(reverse('login')) and not request.path.startswith(reverse('register')) and not request.path.startswith(reverse('about')) and not request.path.startswith(reverse('landing')):
                return redirect(reverse('login'))
            
        elif hasattr(request.user, 'profile'):
            request.role = 'profile'
        
        elif hasattr(request.user, 'staff'):
            request.role = 'staff'
        
        elif hasattr(request.user, 'admin'):
            request.role = 'admin'
            
        else:
            request.role = 'unknown'
        
        response = self.get_response(request)
        return response