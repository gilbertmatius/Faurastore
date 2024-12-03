from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def home(request):
    products = [
        {
            "name": "Blouse Knit Serut",
            "price": "75k",
            "image": "Blouse Knit Serut-75k.jpg",
        },
        {
            "name": "Blouse polo linen",
            "price": "85k",
            "image": "Blouse polo linen-85k.jpg",
        },
        {"name": "Blouse rempel k", "price": "75k", "image": "Blouse rempel k-75k.jpg"},
        {"name": "Blouse", "price": "99k", "image": "Blouse-99k.jpg"},
        {"name": "Carding import", "price": "99k", "image": "Carding import-99k.jpg"},
        {"name": "Carding Knit", "price": "39k", "image": "Carding Knit-39k.jpg"},
        {"name": "Carding", "price": "98k", "image": "Carding-98k.jpg"},
        {
            "name": "Cardingan Korean look",
            "price": "60k",
            "image": "Cardingan Korean look-60k.jpg",
        },
    ]

    return render(request, "main/home.html", {"products": products})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Akun telah dibuat untuk {user.username}. Silakan login."
            )
            return redirect("login")
        else:
            messages.error(request, "Silakan perbaiki kesalahan di bawah.")
    else:
        form = RegisterForm()
    return render(request, "main/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Anda berhasil login sebagai {username}.")
                return redirect("home")
            else:
                messages.error(request, "Username atau password salah.")
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "main/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Anda telah logout.")
    return redirect("home")
