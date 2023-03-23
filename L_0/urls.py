from django.urls import path, include
from django.contrib import admin

urlpatterns = [
path('admin/', admin.site.urls),
    path('lesson/', include('lesson.urls')),
    path('lesson_1/', include('lesson_1.urls')),
    path('lesson_2/', include('lesson_2.urls')),
    # path('lesson_3/', include('lesson_3.urls')),
    path('lesoon_4/', include('lesoon_4.urls')),
    path('lesson_5/', include('lesson_5.urls')),
    path('lesson_6/', include('lesson_6.urls')),
    path('lesson_7/', include('lesson_7.urls'))
]
