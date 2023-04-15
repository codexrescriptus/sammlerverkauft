from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('authors/<author_slug>/', views.author_pictures, name='author-pictures'),
    path('epochs/<epoch_slug>/', views.epoch_pictures, name='epoch-pictures'),
    path('authors/', views.authors, name='authors'),
    path('epochs/', views.epochs, name='epochs'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('<picture_slug>/', views.picture_detail, name='detail-picture'),
    path('', views.pictures, name='pictures'),
]