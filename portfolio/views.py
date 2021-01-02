from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')

def portfolio_page(request):
    return render(request, 'details.html')