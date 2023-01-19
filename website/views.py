from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

def home(request):
    return render(request, 'home.html', {})


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email = EmailMessage(
            "New contact form submission",
            message,
            ['brunaldobani1@gmail.com'],
            ['brunaldobani1@gmail.com'],
            reply_to=[email],
            headers={'Message-ID': 'foo'},
        )
        email.send()
        return redirect('success')
    return redirect('home')

def success(request):
    return render(request, 'success.html')