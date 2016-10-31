from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class ColorScheme(models.Model):

    name = models.CharField(max_length=15)
    snake_R = models.IntegerField(
        verbose_name="Red",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    snake_G = models.IntegerField(
        verbose_name="Green",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    snake_B = models.IntegerField(
        verbose_name="Blue",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    apple_R = models.IntegerField(
        verbose_name="Red",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    apple_G = models.IntegerField(
        verbose_name="Green",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    apple_B = models.IntegerField(
        verbose_name="Blue",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    walls_R = models.IntegerField(
        verbose_name= "Red",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    walls_G = models.IntegerField(
        verbose_name="Green",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    walls_B = models.IntegerField(
        verbose_name="Blue",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    background_R = models.IntegerField(
        verbose_name="Red",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    background_G = models.IntegerField(
        verbose_name="Green",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    background_B = models.IntegerField(
        verbose_name="Blue",
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name

class HighScore(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(
        default=0,
        validators=[
        MinValueValidator(0)
    ])

    def __str__(self):
        return self.name