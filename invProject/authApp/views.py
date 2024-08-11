from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            login(request, user)
            return redirect("authApp:dashboard")
        else:
            messages.error(request, "Invalid Input, please input valid data!")
    else:
        form = RegisterForm()
    
    context = {
        "form": form,
    }
    
    return render(
        request,
        "authApp/accounts/register.html",
        context,
    )

def login_view(request):
    error_message = ""
    if request.method == "POST":
        print("in post")
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        # username = request.POST.get("username")
        # password = request.POST.get("password")
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                next_url = request.POST.get("next") or request.GET.get("next") or "authApp:dashboard"

                return redirect(next_url)
            else:
                messages.error(request, "Invalid Credentials")
                #error_message = "Invalid Credentials"
    else:
        form = LoginForm()
    context = {
        #"error": error_message,
        "form": form,
    }
    
    return render(
        request,
        "authApp/accounts/login.html",
        context,
    )

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("authApp:login")
    else:
        return redirect("authAppp:dashboard")

@login_required
def home_view(request):
    return render(
        request,
        "authApp/authenticated/home.html",
    )

class ProtectedView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    
    def get(self, request):
        return render(
            request,
            "invApp/home.html",
        )