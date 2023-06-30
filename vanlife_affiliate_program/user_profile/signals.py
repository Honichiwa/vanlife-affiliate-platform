from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import Profile

@receiver(user_signed_up)
def sync_google_profile(request, user, **kwargs):
    if user.socialaccount_set.filter(provider='google').exists():
        # Create a profile for the user
        Profile.objects.create(user=user)