from django.contrib import admin
from django.urls import path, include
import post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]
