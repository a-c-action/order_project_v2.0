from django.shortcuts import render

# Create your views here.

def RetrievePassword(request):
    return render(request,"RetrievePassword.html")
