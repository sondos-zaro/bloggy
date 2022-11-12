from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/post/',views.getPost,name='post'),
    path('categories/', views.getCategories),
    path('<int:cat_id>/category/',views.getCategory,name='category'),
]
