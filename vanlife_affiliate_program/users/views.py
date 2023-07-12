from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'In order to sign up, you need to logout first')
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):    
                messages.error(request, error)
                

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "registration/register.html",
        context={"form": form}
    )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

@csrf_protect
def custom_login(request):
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in as <b>{request.user.username}</b>!')
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("home")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="account/login.html",
        context={"form": form}
        )

@login_required
@csrf_protect
def profile(request, username):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, Your profile has been updated!')
            return redirect("profile", user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['about_you'].widget.attrs = {'rows': 1}
        return render(
            request=request,
            template_name="account/profile.html",
            context={"form": form}
            )
    
    return redirect("home")