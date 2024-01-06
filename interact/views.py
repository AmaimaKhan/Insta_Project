# views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Like, Comment
from django.contrib.auth.decorators import login_required

@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    user = request.user
    like, created = Like.objects.get_or_create(photo=photo, user=user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    like_count = Like.objects.filter(photo=photo).count()

    response_data = {
        'liked': liked,
        'count': like_count,
    }

    # Ensure the content type is set to application/json
    return JsonResponse(response_data)



# @login_required
def comment_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        Comment.objects.create(user=request.user, photo=photo, text=text)
    return redirect('interact:photo_detail', photo_id=photo_id)


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    liked = True  # Replace with your logic to determine if the user has liked the photo
    count = Like.objects.filter(photo=photo).count()
    return render(request, 'interact/photo_details.html', {'photo': photo, 'liked': liked, 'count': count})
