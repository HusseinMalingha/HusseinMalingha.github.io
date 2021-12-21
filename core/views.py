from django.shortcuts import render
from django.views.generic import CreateView
from .models import Quote

def index(request):
    return render(request,'core/index.html')

class QuoteCreateView(CreateView):
    model = Quote
    fields = ['full_name', 'company_name', 'email_address', 'service_name', 'description']
