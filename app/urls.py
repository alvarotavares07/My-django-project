from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cards_view  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cards_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


