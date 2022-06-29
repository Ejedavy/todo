import uuid
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

from board.models import Board
from list.models import List
from priorities.models import Priority

User = get_user_model()


# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='items')
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, related_name='items', blank=True, null = True)
    due_time = models.DateTimeField(blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Items"

    def __str__(self):
        return f"Item-{self.name}"

    def clean(self):
        item_names = [item.name.lower() for item in self.list.items.all()]
        if self.name.lower() in item_names:
            raise ValidationError(
                {'name': f"An item named {self.name} already exits in list {self.list.name}"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)