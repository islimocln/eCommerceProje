from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def login_page(request):
    return render(request, 'loginPage.html')

def signup_page(request):
    return render(request, 'signUp.html')
