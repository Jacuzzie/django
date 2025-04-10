from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from datetime import datetime
from .forms import ContactForm
from .models import ChatMessage, Booking
import logging
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

logger = logging.getLogger(__name__)

@login_required
def home(request):
    logger.info(f"User {request.user} accessed the home page.")
    return render(request, 'main/home.html')

# About Page
@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

# Contact Page
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send email, save to DB)
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('main:contact')  # Redirect to contact page after success
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

# My Bookings Page
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, 'main/my_bookings.html', {'bookings': bookings})

# My Energy Page
@login_required
def my_energy(request):
    return render(request, 'main/my_energy.html')

# My Carbon Footprint Page
@login_required
def my_carbon_footprint(request):
    return render(request, 'main/my_carbon_footprint.html')

# Chat Response API
def chat_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').lower()
        ChatMessage.objects.create(sender='user', message=user_message)

        # Simulate dynamic responses
        if "help" in user_message:
            response = "Sure, how can I assist you?"
        elif "booking" in user_message:
            response = "You can view your bookings in the 'My Bookings' section."
        elif "carbon footprint" in user_message:
            response = "Your carbon footprint is calculated based on your energy usage."
        else:
            response = "I'm here to help! Please provide more details."

        ChatMessage.objects.create(sender='bot', message=response)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Consultations Page
@login_required
def consultations(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        topic = request.POST.get('topic')
        consultant = request.POST.get('consultant')

        try:
            time_24hr = datetime.strptime(time, "%I:%M %p").time()
        except ValueError:
            messages.error(request, 'Invalid time format. Please select a valid time.')
            return redirect('main:consultations')

        if service and date and time_24hr and topic and consultant:
            Booking.objects.create(
                service=service,
                date=date,
                time=time_24hr,
                topic=topic,
                consultant=consultant,
                user=request.user  # Associate booking with the logged-in user
            )
            messages.success(request, 'Your consultation has been booked successfully!')
            return redirect('main:consultations')
        else:
            messages.error(request, 'Please fill out all fields before booking.')

    return render(request, 'main/consultations.html')

# Cancel Booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, 'Booking canceled successfully.')
    return redirect('main:my_bookings')

# Signup Page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')  # Redirect to home after signup
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


# Debug Login View (Optional for Debugging)
class DebugLoginView(LoginView):
    template_name = 'main/login.html'

    def get(self, request, *args, **kwargs):
        print(f"Using template: {self.template_name}")
        return super().get(request, *args, **kwargs)

def debug_root(request):
    return HttpResponse("Root URL is working!")

##
def solar_panels(request):
    return render(request, 'main/solar_panels.html')

def ev_chargers(request):
    return render(request, 'main/ev_chargers.html')

def smart_home_devices(request):
    return render(request, 'main/smart_home_devices.html')

def my_carbon_footprint(request):
    return render(request, 'main/my_carbon_footprint.html')
##

@login_required
def account_info(request):
    return render(request, 'main/account_info.html', {'user': request.user})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Keep the user logged in
            return redirect('main:account_info')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'main/change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('main:home')
    return render(request, 'main/delete_account.html')