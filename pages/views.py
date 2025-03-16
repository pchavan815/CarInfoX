from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from CarDealer Website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'darshankadam153@gmail.com',
                [admin_email],
                fail_silently=True,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')


def emi(request):

    return render(request, 'pages/emi.html')

def car_emi_calculator(request):
        # Get values from query parameters and convert to float
        amount = float(request.GET.get("amount", 0))
        interest = float(request.GET.get("interest", 0))
        tenure = float(request.GET.get("tenure", 0))

        # Calculate monthly interest rate
        monthly_interest_rate = (interest / 12) / 100

        # Calculate EMI
        if amount > 0 and interest > 0 and tenure > 0:
            emi = (amount * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure) / \
                  ((1 + monthly_interest_rate) ** tenure - 1)

            emi = round(emi, 2)
        else:
            emi = 0

        # Pass the calculated EMI to the template
        context = {'emi': emi, 'amount': amount, 'interest': interest, 'tenure': tenure}
        return render(request, 'pages/emi.html', context)

def accessories(request):

    return render(request,'pages/accessories.html')

