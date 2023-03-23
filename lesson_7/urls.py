from django.urls import include, path
from rest_framework import routers
from lesson_7 import views

router = routers.SimpleRouter()
router.register(r'view-set', views.ViewSetAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('function/', views.view_function, name='function_view'),
    path('class/', views.ClassAPIView.as_view(), name='class_view'),
    path('generic/', views.MyCreateAPIView.as_view(), name='generic'), #create user
    path('retrive/<int:pk>', views.MyRetrieveAPIView.as_view(), name='retrive'),
    path('retrive-update/<int:pk>', views.MyRetrieveUpdateAPIView.as_view(), name='retrive-update'),
    path('api-login', views.user_login),
    path('create-user', views.CreateUser.as_view())
]