from django import forms
from django.utils import timezone
from django.db import models
from django.urls import reverse


class Quote(models.Model):
    SERVICE_CHOICES = [
    ('WD','Website development'),
    ('DM','Digital Marketing'),
    ('SD','Systems Development'),
]
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=254)
    service_name = models.CharField(max_length=2,choices=SERVICE_CHOICES)
    description = models.TextField(max_length=250)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('home')
    
