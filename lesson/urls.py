from django.urls import path
from lesson.views import index

urlpatterns = [
    path('', index, name = "index"),
]