"""
User Profile Management Models
Contains the user profile model and related functionality for managing
user account information beyond the basic Django User model. Extends user
data to include delivery addresses, contact information, and order history.
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Extended user profile model for storing delivery and personal information.
    Extends the Django User model to store additional information specific
    to the e-commerce application. Includes delivery addresses, contact
    information, and user preferences that enhance the shopping experience.
    Automatically created when a user registers through the post_save signal.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_country = CountryField(
        blank_label='Country', null=True, blank=True
    )

    def __str__(self):
        """Return the username as string representation."""
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create or update user profiles.
    Ensures that every user has an associated UserProfile instance.
    Creates a profile when a new user is created, or ensures the profile
    exists when an existing user is updated.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        profile, _ = UserProfile.objects.get_or_create(user=instance)
        profile.save()
