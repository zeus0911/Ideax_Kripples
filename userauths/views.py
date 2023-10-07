from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your views here.
def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            newuser = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey{username}, Your Account is created Sucessfuly!")
            newuser = authenticate(username=form.cleaned_data['email'],
                                   password=form.cleaned_data['password1'],
                                   
            )
            login(request, newuser)
            return redirect("app:index")        
    else:
        form = UserRegisterForm()

    
    context = {
        'form' : form,
    }
    return render(request, 'signup.html',context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey! You are already logged in!!")
        return redirect("app:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")


        try:
            user = User.objects.get(email = email)
        except:
           pass

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are loggged in!")
            return redirect("app:index")
        else:
            messages.warning(request, "User Doesn't exist!!")

    context = {

    }

    return render(request, "sign-in.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You are loggged Out!!")
    return redirect("userauths:login")