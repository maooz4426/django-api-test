from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()

    def __str__(self):
        return self.name