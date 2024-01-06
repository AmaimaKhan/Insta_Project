# interactions/urls.py
from django.urls import path
from .views import like_photo, comment_photo, photo_detail

app_name = 'interact'
urlpatterns = [
    path('like_photo/<int:photo_id>/', like_photo, name='like_photo'),
    path('comment_photo/<int:photo_id>/', comment_photo, name='comment_photo'),
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),
    # Add more interaction-related URLs as needed
]
