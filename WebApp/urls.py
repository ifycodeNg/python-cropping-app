
from django.contrib import admin
from django.urls import path
from django.conf import settings
from croppingApp.views import photo_list
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', photo_list,name='photo_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
