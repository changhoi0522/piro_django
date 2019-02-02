from django.conf import settings
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='accounts/login_form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),
    path('profile/', views.profile, name='profile'),

]