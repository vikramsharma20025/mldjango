from django.contrib import admin
from django.urls import path,include
from facedetection import views

urlpatterns = [
    path('facedetection',views.detectface,name='detectface'),    
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
