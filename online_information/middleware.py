from django.utils.cache import add_never_cache_headers
from django.conf import settings


class NoCacheMiddleware:
    """
    Middleware to prevent caching in development mode.
    This helps avoid issues with cached Cloudinary URLs or other media file problems.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Only apply no-cache headers in DEBUG mode
        if settings.DEBUG:
            add_never_cache_headers(response)
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        
        return response
