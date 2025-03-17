from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send email, save to DB)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Example: Here you could send an email or save to DB
            # For now, just show success message
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('main:contact')  # redirect to contact page after success
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})
