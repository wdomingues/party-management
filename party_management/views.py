from django.conf import settings
from django.shortcuts import redirect, render
from django.utils import timezone
from django.core.mail import send_mail

from party_guests.forms import GuestForm
from party_guests.models import Guest

from twilio.rest import Client

def index(request):
    sentence = "This sentence is from index.html"
    return render(request, 'index.html', {'sentence': sentence})


def register_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_guests')
    else:
        form = GuestForm()
    return render(request, 'register_guest.html', {'form': form})


def list_guests(request):
    guests = Guest.objects.all()
    return render(request, 'list_guests.html', {'guests': guests})


def send_confirmations(request): #TODO fix for 3 confirmations
    confirmation_date = timezone.now() + timezone.timedelta(days=7)  # TODO Change for setup date
    guests = Guest.objects.filter(confirmed_1=False) #TODO fix for 3 confirmations

    for g in guests:
        send_mail(
            'Confirmação de Presença',
            'Olá {}, confirme sua presença na festa até {}'.format(g.name, confirmation_date),
            settings.EMAIL_HOST_USER,
            [g.email],
            fail_silently=False,
        )

    account_sid = settings.WPP_ACC_SID
    auth_token = settings.WPP_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=f'whatsapp:{ settings.WPP_FROM_NUM }',
        body='Your appointment is coming up on July 21 at 3PM',
        to=f'whatsapp:{g.cellphone}'
    )
    print(message.sid)
    
    g.confirmed_1 = True
    g.save()

    return redirect('list_guests')