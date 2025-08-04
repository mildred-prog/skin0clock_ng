"""
Custom Error Handler Views
Contains custom error handler views for the Django application.
Provides user-friendly error pages when HTTP errors occur, replacing
default Django error pages with custom templates for better UX.
"""
from django.shortcuts import render


def handler404(request, exception):
    """
    Custom 404 error handler for page not found errors.
    Handles cases where users try to access pages that don't exist.
    Renders a custom 404 error page instead of the default Django error page.
    """
    return render(request, "errors/404.html", status=404)


def handler400(request, exception):
    """
    Custom 400 error handler for bad request errors.
    Handles cases where the server cannot process the request due to
    client error. Renders a custom 400 error page to inform users.
    """
    return render(request, "errors/400.html", status=400)


def handler403(request, exception):
    """
    Custom 403 error handler for forbidden access errors.
    Handles cases where users try to access resources they don't have
    permission to view. Renders a custom 403 error page.
    """
    return render(request, "errors/403.html", status=403)


def handler500(request):
    """
    Custom 500 error handler for internal server errors.
    Handles unexpected server errors that occur during request processing.
    Renders a custom 500 error page to inform users about server issues.
    """
    return render(request, "errors/500.html", status=500)
