from django.db import models
from django.db.utils import ProgrammingError
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


