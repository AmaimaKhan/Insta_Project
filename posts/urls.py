# photos/urls.py
from django.urls import path
from .views import upload_photo
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('upload_photo/', upload_photo, name='upload_photo'),
    # Add more photo-related URLs as needed
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)