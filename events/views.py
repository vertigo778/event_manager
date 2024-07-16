from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Entry
from .forms import EventForm, EntryForm
from django.conf import settings
from twilio.rest import Client
from django.template.defaulttags import register
from django.contrib.auth import logout
from django.shortcuts import render
import os

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')




@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={"class": class_name})


def home(request):
    return render(request, 'events/home.html')


def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()  # The save method will automatically set the order
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/event_list.html', {'events': events})



@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})



from textmagic.rest import TextmagicRestClient
username = "spxsignals"
token = "xWMQ2KW63O0UuA6JWLbdG32ZoffqBn"
client = TextmagicRestClient(username, token)
#message = client.messages.create(phones="+16612210015", text="Hello TextMagic")

TURN_OFF = True

def sendtext(content, number):

    if len(number) == 10:
        message = client.messages.create(phones=("+1" + number), text=content)


# Add this function to send SMS
def send_sms(phone_number, message):
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)
    entries = Entry.objects.filter(event=event)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.event = event
            entry.save()  # The save method will automatically set the order
            # Send SMS when added to the list
            message = f"You've been added to the waitlist for {event.title}. We'll notify you when your status changes."
            send_sms(entry.phone_number, message)
            return redirect('event_detail', event_id=event.id)
    else:
        form = EntryForm()
    return render(request, 'events/event_detail.html', {'event': event, 'entries': entries, 'form': form})

@login_required
def update_entry_status(request, entry_id, status):
    entry = get_object_or_404(Entry, id=entry_id, event__organizer=request.user)
    old_status = entry.status
    entry.status = status
    entry.save()
    
    if old_status == 'WAITING':
        if status == 'ACCEPTED':
            message = f"Congratulations! You've been accepted to {entry.event.title}. Head to UCB LA for your ticket."
        elif status == 'REJECTED':
            message = f"We're sorry, we don't have a ticket for you for {entry.event.title} ."
        
        send_sms(entry.phone_number, message)
    
    return redirect('event_detail', event_id=entry.event.id)

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, event__organizer=request.user)
    event_id = entry.event.id
    if request.method == 'POST':
        # Send SMS notification
        message = f"Your entry for the event '{entry.event.title}' has been removed."
        #send_sms(entry.phone_number, message)
        
        entry.delete()
        return redirect('event_detail', event_id=event_id)
    return render(request, 'events/delete_entry.html', {'entry': entry})