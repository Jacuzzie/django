from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    # Home page (if needed, uncomment and define the `home` view in views.py)
    # Home page
    path('home/', views.home, name='home'),  # Add this line for /home/ URL

    # About and contact pages
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),

    # Dashboard-related URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/my-bookings/', views.my_bookings, name='my_bookings'),
    path('dashboard/my-bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('dashboard/my-energy/', views.my_energy, name='my_energy'),
    path('dashboard/my-carbon-footprint/', views.my_carbon_footprint, name='my_carbon_footprint'),

    # Other views
    path('chat-response/', views.chat_response, name='chat_response'),
    path('consultations/', views.consultations, name='consultations'),

    # Authentication-related URLs
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    #Products and services pages
    path('solar-panels/', views.solar_panels, name='solar_panels'),
    path('ev-chargers/', views.ev_chargers, name='ev_chargers'),
    path('smart-home-devices/', views.smart_home_devices, name='smart_home_devices'),
    path('my-carbon-footprint/', views.my_carbon_footprint, name='my_carbon_footprint'),

    #Account information page
    path('account-info/', views.account_info, name='account_info'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),

]
