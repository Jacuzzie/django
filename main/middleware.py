from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    """
    Middleware to ensure that users are logged in before accessing any page.
    Excludes paths like LOGIN_URL, SIGNUP_URL, and LOGOUT_URL.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define excluded paths that don't require authentication
        excluded_urls = [
            settings.LOGIN_URL,  # Login page
            '/signup/',          # Signup page
            settings.LOGOUT_REDIRECT_URL,  # Logout redirect
        ]

        # Resolve the current URL name
        try:
            current_url_name = resolve(request.path).url_name
        except:
            current_url_name = None

        # Debugging logs
        print(f"Current path: {request.path}")
        print(f"Resolved URL name: {current_url_name}")
        print(f"User authenticated: {request.user.is_authenticated}")

        # Allow access to excluded URLs or static files
        if (
            request.path in excluded_urls or
            current_url_name in ['login', 'signup', 'logout'] or
            request.path.startswith('/static/')  # Allow static files
        ):
            return self.get_response(request)

        # Redirect unauthenticated users to the login page
        if not request.user.is_authenticated:
            print("Redirecting to login page...")
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)