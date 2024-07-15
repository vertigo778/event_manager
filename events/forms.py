from django import forms
from .models import Event, Entry
import re

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class EntryForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=10,
        min_length=0,
        widget=forms.TextInput(attrs={'placeholder': 'Enter 10-digit number'}),
    )

    class Meta:
        model = Entry
        fields = ['name', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d{10}$', phone_number):
            raise forms.ValidationError('Phone number must be 10 digits.')
        return phone_number