# users/urls.py
from django.urls import path
from.import views
from .views import edit_profile, view_profile, index, view_follow

app_name = "user_profile"

urlpatterns = [
    path("", index, name='index'),
    path ("UserProfile/", views.index_view, name=" UserProfile"),
    path('follow/<int:user_id>/', view_follow, name='toggle_follow'),
    path('edit/', edit_profile, name='edit_profile'),
    path('view/', view_profile, name='view_profile'),
    path("signup/", views.sign_up, name="sign_up"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Add more user-related URLs as needed
    
]