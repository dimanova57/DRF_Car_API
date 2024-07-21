from django.db import models

class Car(models.Model):
    model = models.CharField('model', max_length=100, unique=True)
    year = models.IntegerField('year')

    def __str__(self) -> models.CharField:
        return self.model
