from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    # Home page (if needed, uncomment and define the `home` view in views.py)
    # path('', views.home, name='home'),

    # About and contact pages
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),

    # Dashboard-related URLs
    path('dashboard/my-bookings/', views.my_bookings, name='my_bookings'),
    path('dashboard/my-bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('dashboard/my-energy/', views.my_energy, name='my_energy'),
    path('dashboard/my-carbon-footprint/', views.my_carbon_footprint, name='my_carbon_footprint'),

    # Other views
    path('chat-response/', views.chat_response, name='chat_response'),
    path('consultations/', views.consultations, name='consultations'),

    # Authentication-related URLs
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),  # Root URL for the home page
]