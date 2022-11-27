
# from django.shortcuts import render, redirect

# from .models import Photo
# from .forms import PhotoForm


# def photo_list(request):
#     photos = Photo.objects.all()
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('photo_list')
#     else:
#         form = PhotoForm()
#     return render(request, 'photo_list.html', {'form': form, 'photos': photos})




from django.shortcuts import render, redirect
from PIL import Image
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        x = float(request.POST.get('x',False))
        y = float(request.POST.get('y',False))
        w = float(request.POST.get('width',False))
        h = float(request.POST.get('height',False))
        category = request.POST.get('category',False)
        picture=request.FILES.get('image') 
        photo= Photo(file=picture.name,category=category)      
        photo.save()
        image = Image.open(picture)
        cropped_image=image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS) 
        resized_image.save(photo.file.path)
        return redirect('/')
    else:

     return render(request, 'photo_list.html', { 'photos': photos})