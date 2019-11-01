from django.contrib import admin
from django.urls import include, path
from logbook import views

urlpatterns = [
    path('', include('logbook.urls')),
    path('admin/', admin.site.urls),
]