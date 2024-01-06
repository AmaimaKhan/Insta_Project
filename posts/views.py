# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from posts.models import Photo

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('interact:photo_detail', photo_id=photo.pk)  # Use 'photo_id' instead of 'photo_'
    else:
        form = PhotoForm()
    return render(request, 'posts/upload_photo.html', {'form': form})
