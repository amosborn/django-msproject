from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from lots.models import Auction
from django.utils import timezone
from .models import Profile


def index(request):
    """Return index.html page"""
    return render(request, 'index.html')


@login_required
def logout(request):
    """Log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('index'))


def login(request):
    """Return login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                                     "Username or password is incorrect.")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """Return registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request,
                               "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {"registration_form": registration_form})


@login_required
def user_profile(request):
    """User's profile page"""

    user = User.objects.get(email=request.user.email)
    current_auctions = Auction.objects.filter(winning_bidder=request.user.pk,
                                              auction_end_time__gte=timezone.now())
    past_auctions = Auction.objects.filter(winning_bidder=request.user.pk,
                                           auction_end_time__lt=timezone.now())

    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated.')
        else:
            messages.error(request, 'Unable to update profile.')

    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile_form': profile_form,
                  'current_auctions': current_auctions, 'past_auctions': past_auctions})
