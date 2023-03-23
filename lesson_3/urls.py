from django.urls import path
from lesson_3 import views

urlpatterns = [
    path('create-flower/', views.CreateFlower, name="create-flower"),
    path('create-client/', views.CreateClient, name="create-client"),
    path('get-flower/', views.GetFlower, name="get-flower"),
]

