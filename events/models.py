from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.order == 0:
            last_order = Event.objects.filter(organizer=self.organizer).aggregate(models.Max('order'))['order__max']
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

class Entry(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[
        ('WAITING', 'Waiting'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('GIVEN_TICKET', 'Given Ticket')
    ], default='WAITING')

    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.name} - {self.event.title}"

    def save(self, *args, **kwargs):
        if self.order == 0:
            last_order = Entry.objects.filter(event=self.event).aggregate(models.Max('order'))['order__max']
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.event.title}"