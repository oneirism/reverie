from django.db import models

from autoslug import AutoSlugField


class Campaign(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)

    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Faction(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    campaign = models.ForeignKey(Campaign)

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)

    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    campaign = models.ForeignKey(Campaign)

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)

    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    campaign = models.ForeignKey(Campaign)

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)

    description = models.CharField(max_length=500)
    faction = models.ForeignKey(Faction, blank=True, null=True)
    location = models.ForeignKey(Location, related_name='location')
    previous_locations = models.ManyToManyField(Location, related_name='previous_locations', blank=True)

    def __str__(self) -> str:
        return self.name
