from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extends Django default user (username, email, etc.)
    pass

    def __str__(self):
        return self.username


class TransitLine(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lines")
    line_name = models.CharField(max_length=100)
    line_color = models.CharField(max_length=7, default="#3B82F6")  # HEX

    def __str__(self):
            return f"{self.owner}.{self.line_name}"

class Station(models.Model):
    line = models.ForeignKey(TransitLine, on_delete=models.CASCADE, related_name="stations")
    station_name = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(default=1)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
                return self.station_name

    class Meta:
        ordering = ['display_order']

class UserLocationState(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="current_location")
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friendships")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="related_friendships")
    status = models.CharField(max_length=20, default="accepted")
    created_at = models.DateTimeField(auto_now_add=True)
