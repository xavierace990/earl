# urls.py

from django.urls import path
from . import views
from app.forms import UserLoginForm
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    #path('results/', views.results, name='results'),
    path('accounts/profile/', views.profile, name='profile'),
    path('form/', views.form, name='form'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('success/', views.success, name='success'),
    path('signup/', views.signup, name='signup'),
    # Add other URLs as needed
]