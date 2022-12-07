

from django.shortcuts import render, redirect
from PIL import Image
import uuid
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        x = float(request.POST.get('x',False))
        y = float(request.POST.get('y',False))
        w = float(request.POST.get('width',False))
        h = float(request.POST.get('height',False))
        rotation = int(request.POST.get('rotation',False)) * -1
        category = request.POST.get('category',False)
        picture=request.FILES.get('image') 
        image_name=str(uuid.uuid4())+'.'+picture.name.split(".")[-1]
        photo= Photo(file=image_name,category=category)     
        photo.save()
        image = Image.open(picture)
        cropped_image=image.crop((x, y, w+x, h+y))
        rotated_image=cropped_image.rotate(rotation)
        resized_image = rotated_image.resize((200, 200), Image.ANTIALIAS) 
        resized_image.save(photo.file.path)
        return redirect('/')
    else:

     return render(request, 'photo_list.html', { 'photos': photos})