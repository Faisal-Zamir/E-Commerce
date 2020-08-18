from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout , name="logout"),

]
