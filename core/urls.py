from django.urls import path
from .views import QuoteCreateView
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('quote/new/', QuoteCreateView.as_view(), name='quote-create')
]