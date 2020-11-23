from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    user= request.user
    print(user)

 
    return render(request, 'home.html',{'user':user})

