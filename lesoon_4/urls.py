from django.urls import path
from lesoon_4 import views

urlpatterns = [
    path('try-form/', views.my_form, name="try-form"),
    path('class-form/', views.MyFormView.as_view(), name = "class-form"),
    path('try-model-form', views.ModelFormView.as_view(), name = "try-model-form")
]
