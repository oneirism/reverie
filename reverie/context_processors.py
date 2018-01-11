from django.conf import settings

def google_analytics(request):
    ga_key = getattr(settings, 'GOOGLE_ANALYTICS_KEY')
    if not settings.DEBUG and ga_key:
        return {
            'GOOGLE_ANALYTICS_KEY': ga_key,
        }
    return {}
