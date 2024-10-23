from django.shortcuts import render

# Create your views here.
def HouseOnline(request):

    return render(request,'index.html')

def login(request):

    return render(request,'login.html')