
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),  # Halaman web
    path('api/login/', views.login, name='login'),        # API Login
    path('api/logout/', views.logout, name='logout'),     # API Logout
]
