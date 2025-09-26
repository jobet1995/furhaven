"""
URL configuration for furhaven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.http import require_GET
from django.db import connection

@require_GET
def health_check(request):
    """Health check endpoint for monitoring."""
    try:
        # Check database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = True
    except Exception as e:
        db_status = False
    
    status_code = 200 if db_status else 503
    return JsonResponse(
        {
            'status': 'healthy' if db_status else 'unhealthy',
            'db_status': 'connected' if db_status else 'disconnected',
            'debug': settings.DEBUG,
        },
        status=status_code
    )

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>FurHaven - Pet Adoption Platform</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; text-align: center; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #4a6fa5; }
            .status { color: #2e7d32; font-weight: bold; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to FurHaven</h1>
            <p>Your Django application is running successfully with Gunicorn and Nginx!</p>
            <div class="status">✓ Django is working correctly</div>
            <p>You can now proceed to the <a href="/admin/">admin panel</a>.</p>
        </div>
    </body>
    </html>
    """, content_type="text/html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('health/', health_check, name='health_check'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
