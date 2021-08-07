from django.urls import path
from . import views

from .views import HomePageView, AboutPageView, CategoryPageView
 
urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('income/create/', views.create),
    path('income/', views.index, name='index'),
    path('expenses/', views.index_expenses, name='expenses'),
    path('expenses/create_expenses/', views.create_expenses),
    path('category/', CategoryPageView.as_view(), name='category_list'),
    path('', HomePageView.as_view(), name='home'),
]