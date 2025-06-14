from django.urls import path
from . import views 



app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('search/', views.search, name='search'),
    path('create/', views.create_news, name='create_news'),
    path('news/<slug:slug>/update/', views.update_news, name='update_news'),
    path('news/<slug:slug>/delete/', views.delete_news, name='delete_news'),
    
]



