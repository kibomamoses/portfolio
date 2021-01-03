from django.shortcuts import render
import json

import requests

from .models import Contact

def home_page(request):
    return render(request, 'index.html')

def portfolio_page(request):
    return render(request, 'details.html')
    
    
def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'thank.html')
  
 