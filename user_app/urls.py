from django.urls import path
from . import views

app_name = 'user_app' 

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user_view, name='logout'),
    path('register/', views.register_user_view, name='register'),

]





