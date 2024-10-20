from django.urls import path
from .views import tutorial_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tutorial_list, name='tutorial_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
