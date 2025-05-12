from django.db import models

# Create your models here.

class Dress(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='dresses/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    