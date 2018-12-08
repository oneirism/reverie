""" Reverie campaign model definitions. """

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Campaign(models.Model):
    """ A Reverie campaign. """
    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=500,
    )

    game_master = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='gm'
    )

    players = models.ManyToManyField(
        User,
        related_name='player',
        blank=True,
        null=True,
    )

    public = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name


class Character(models.Model):
    """ A Reverie campaign character. """
    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=500,
    )

    player = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Faction(models.Model):
    """ A Reverie campaign faction. """
    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=500,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Item(models.Model):
    """ A Reverie campaign item. """
    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        unique=True,
        max_length=50,
    )

    description = models.TextField(
        max_length=500,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    """ A Reverie campaign location. """
    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        unique=True,
        max_length=50,
    )

    description = models.TextField(
        max_length=500,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Log(models.Model):
    """ A Reverie campaign log entry. """
    title = models.CharField(
        unique=True,
        max_length=50,
    )

    description = models.TextField(
        max_length=5000,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    date = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
