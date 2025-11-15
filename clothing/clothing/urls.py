"""clothing URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.urls import path, include
from django.urls import path, include, re_path

from django.contrib.sitemaps.views import sitemap

from backend.sitemaps import ProductSitemap

sitemaps = {
    "products": ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Admin Dashboard (Custom Admin Panel)

re_path(r'^admin/dashboard/?', include('backend.admin_urls')),

    # Main website URLs
    path('', include('backend.urls')),

    # Django Allauth Authentication URLs
    path('accounts/', include('allauth.urls')),

    # Sitemap
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]

# Serve Media Files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
