from django.urls import path, include
from rest_framework import routers
from lesson_6 import views

router = routers.SimpleRouter()
router.register(r'game', views.GameViewSet)
router.register(r'gamer', views.GamerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
