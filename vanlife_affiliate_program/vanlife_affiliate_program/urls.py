from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from conversions.views import home

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('conversions/', include('conversions.urls')),
    path('profile/', include('user_profile.urls')),
    path('accounts/', include('allauth.urls')),
]+ (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
