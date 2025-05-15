from django.urls import path
from . import views 
from django.views.generic import DeleteView, UpdateView
from .views import NewsDeleteView


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    # path('search/', views.search, name='search'),
    # path('create/', views.create_news, name='create_news'),

    # path('new-update/<int:pk>',  views.NewsUpdateView.as_view(), name='update_news'),

    # path('news-delete/<int:pk>',views.NewsDeleteView.as_view(), name='delete_news')
    
]



