from django.db import models

class TimeSlot (models.model):
    """A time slot that user can choose of"""
    text = models.TextField(max_length=200)
