from django.urls import path
from .views import RegisterView, LoginView, login_view, register_view, home_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('api/register', RegisterView.as_view()),
    path('api/login', LoginView.as_view()),
]