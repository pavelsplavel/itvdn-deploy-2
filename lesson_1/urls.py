from django.urls import path
from lesson_1 import views

urlpatterns = [
    path('index/', views.index, name = 'index-view'),
    path('bio/<username>/', views.bio, name = 'bio-view'),
]