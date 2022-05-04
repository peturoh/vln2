from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999, blank=True)
    avg_rating = models.FloatField(default=None, blank=True, max_length=4)
    profile_bio = models.CharField(max_length=250, blank=True)


