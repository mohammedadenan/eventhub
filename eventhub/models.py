from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookingRequest(models.Model):
    event_name=models.CharField(max_length=100)
    EVENT_TYPE=[
        ('wedding','Wedding'),
        ('engagement','Engagement'),
        ('reception','Reception'),
        ('birthday','Birthday'),
        ('anniversary','Anniversary'),
        ('iftar','Iftar'),
        ('onam','Onam'),
        ('housewarming','Housewarming'),
        ('party','Party'),
        ('other','Other')
    ]
    event_type=models.CharField(max_length=100,choices=EVENT_TYPE)
    date=models.DateField()
    time=models.TimeField()
    BOOKING_SATUS=[
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected')
    ]
    status=models.CharField(max_length=100,choices=BOOKING_SATUS)
    
    FOOD_TYPES = [
        ('vegetarian','Vegetarian'),
        ('non-vegetarian','Non-Vegetarian'),
        ('both', 'Both'),
        ('no food', 'No Food'),
        ('other', 'Other')
    ]
    food=models.CharField(max_length=100,choices=FOOD_TYPES)
    rejection_resson=models.TextField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    
    VENUE_TYPES = [
        ('auditorium','Auditorium'),
        ('convention centre','Convention Centre'),
        ('wedding hall', 'Wedding Hall'),
        ('Community hall', 'Community Hall'),
        ('hotel', 'Hotel'),
        ('resort', 'Resort'),
        ('banquet hall', 'Banquet Hall'),
        ('open ground', 'Open Ground'),
        ('restaurant', 'Restaurant'),
        ('home', 'Home'),
        ('other', 'Other')

    ]
    venue=models.CharField(max_length=100,choices=VENUE_TYPES)

    def __str__(self):
        return self.event_type


class Event(models.Model):


    location=models.CharField(max_length=100)

    amount=models.FloatField()

    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]

    
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='Upcoming')
     
    organizer=models.ForeignKey(User,on_delete=models.CASCADE)
    booking=models.ForeignKey(BookingRequest,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.booking)
