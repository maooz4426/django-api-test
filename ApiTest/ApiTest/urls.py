
from django.contrib import admin
from django.urls import path,include#includeを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('storage/',include('storage.urls')),#追加
]
