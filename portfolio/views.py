from django.shortcuts import render


from .models import Contact

def home_page(request):
    return render(request, 'index.html')

def portfolio_page(request):
    return render(request, 'details.html')
    
    
def contact(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(name_r,email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'thank.html')
  
 