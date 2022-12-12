from django.shortcuts import render,redirect
from . models import*
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method=="POST":
        data = request.POST
        username = data['username']
        password = data['password']
        email = data['email']
        user = User.objects.filter(username=username, email=email)
        if len (user) > 0:
            return render(request, 'signin.html', {'error':'username already exist'})
        else:
            new_user = User.objects.create(username=username, password=password, email=email)
            new_user.save()
            return redirect('signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method=="POST":
        data = request.POST
        username = data['username']
        password = data['password']
        user = User.objects.filter(username=username)
        if len (user) > 0:
            first_user = user.first()
            if first_user.password==password:
                request.session["username"] = username
                details = User.objects.filter(username=username).values()
                if details:
                    return render(request, 'products_page.html', {"details":details})
                return render(request, 'homepage.html', {"info":"not logged in"})
            else:
                return render(request, 'signin.html', {"error": "wrong password"})
        else:
            return render(request, 'signin.html', {"message": "user does not exist"})
    return render(request, 'signin.html')
            

def home(request):
    return render(request, 'homepage.html')
