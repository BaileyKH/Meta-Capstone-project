from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_items, name='menu_item'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about')
]