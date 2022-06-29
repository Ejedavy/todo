import uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Priority(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="priorities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Priorities"


class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    time_before = models.PositiveIntegerField(blank=False)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="reminders", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Reminders"
