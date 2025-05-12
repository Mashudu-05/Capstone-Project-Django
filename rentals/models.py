from django.db import models

class Dress(models.Model):
    """
    Represents a maternity dress available for rental.

    Attributes:
        name (CharField): Name/title of the dress.
        description (TextField): Detailed description of the dress.
        price_per_day (DecimalField): Rental price per day in currency.
        image (ImageField): Image of the dress uploaded to 'dresses/' directory.
        available (BooleanField): Indicates whether the dress is available for rent.
    """

    name = models.CharField(max_length=200)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='dresses/')
    available = models.BooleanField(default=True)

    def __str__(self):
        """
        Return a string representation of the dress object.

        Returns:
            str: Name of the dress.
        """
        return self.name
