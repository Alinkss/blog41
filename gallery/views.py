from django.shortcuts import render, redirect

from gallery.models import Photo
from blog2.views import get_categories
from .forms import PhotoForm

def gallery(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos
    }
    context.update(get_categories())

    return render(request, 'gallery/index.html', context)

def uploads(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    form = PhotoForm()
    context = {
        'form': form,
    }
    return render(request, 'gallery/upload.html', context)
