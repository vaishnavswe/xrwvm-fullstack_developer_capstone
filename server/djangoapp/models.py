# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)

    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPE_CHOICES,
        default=SUV
    )

    year = models.IntegerField(
        default=now().year,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(now().year)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"

