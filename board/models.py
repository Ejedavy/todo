import uuid
from django.contrib.auth import get_user_model

from django.db import models
from rest_framework.exceptions import ValidationError

User = get_user_model()


# Create your models here.
class Board(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Boards"

    def __str__(self):
        return f"Board-{self.name}"

    def clean(self):
        board_names = [board.name.lower() for board in self.created_by.boards.all()]
        if self.name.lower() in board_names:
            raise ValidationError(
                {'name': f"{self.created_by} already has a board named {self.name}"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)