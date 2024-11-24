from django.urls import path
from .views import (
    index,
    login_check
) 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_check, name='login_check')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)