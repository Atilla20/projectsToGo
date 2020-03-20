from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('toGo/', include('toGo.urls')),
    path('admin/', admin.site.urls),
]
