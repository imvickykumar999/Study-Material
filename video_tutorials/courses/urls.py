from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.folder_list, name='folder_list'),
    path('folders/<str:folder>/', views.tutorial_list, name='tutorial_list'),
    path('tutorial/<int:pk>/', views.tutorial_detail, name='tutorial_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
