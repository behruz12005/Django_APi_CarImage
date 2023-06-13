from django.urls import path
from .views import Home,addItem,livecam_feed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name='home'),
    path('add/', addItem, name='add'),
    path('livecam_feed', livecam_feed, name='livecam_feed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

