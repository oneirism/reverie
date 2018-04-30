from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('campaign/', include('campaign.urls'))
    path('', include('splash.urls'))
]