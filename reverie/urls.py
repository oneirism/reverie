from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include(('splash.urls', 'splash'), namespace='splash')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('campaign/', include(('campaign.urls', 'campaign'), namespace='campaign')),
    path('markdownx/', include(('markdownx.urls', 'markdownx'), namespace='markdown')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # pragma: no cover
