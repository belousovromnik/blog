from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import include, path

from app import views

urlpatterns = [
    path('posts/', include(('app.urls', 'posts'))),
    path('admin/', admin.site.urls),
]
