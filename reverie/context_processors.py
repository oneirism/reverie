from django.conf import settings


# Google Analytics Context
def google_analytics(request):
    #pylint: disable=unused-argument
    return {
        'GOOGLE_ANALYTICS_KEY': getattr(
            settings, 'GOOGLE_ANALYTICS_KEY', None
        ),
    }
