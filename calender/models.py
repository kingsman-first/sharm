from django.db import models


class Services(models.Model):
    """A services that user can choose of"""
    text = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


