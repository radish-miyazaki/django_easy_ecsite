from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from allauth.socialaccount.providers.google.urls import urlpatterns as google_url

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
    path('admin/', admin.site.urls),
    path('oauth_accounts/', include(google_url)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
