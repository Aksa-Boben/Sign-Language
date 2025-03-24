from django.urls import path
from . import views

app_name = 'translator'  # Ensures namespacing works correctly

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('translate/', views.translate, name='translate'),
]
