import uuid
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

from board.models import Board

User = get_user_model()


# Create your models here.
class List(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Lists"

    def __str__(self):
        return f"List-{self.name}"

    def clean(self):
        list_names = [single_list.name.lower() for single_list in self.board.lists.all()]
        if self.name.lower() in list_names:
            raise ValidationError(
                {'name': f"A list named {self.name} already exits in Board-{self.board.name}"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
