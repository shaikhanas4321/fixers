from django.db import models
from django.contrib.auth.models import AbstractUser
from services.models import skills 
# Create your models here.
class User(AbstractUser):
    user_type_choices =(
    ('CUSTOMER', 'Customer'),
    ('PROVIDER', 'Provider')
    )
    user_type = models.CharField(max_length=20, choices=user_type_choices)
    profile_completed=models.BooleanField(default=False)
 


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ForeignKey(skills, on_delete=models.PROTECT , null=True , blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    is_active=models.BooleanField(default=False)
