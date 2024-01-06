# forms.py
from django import forms
from .models import UserProfile, Follow

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ['followed_user']