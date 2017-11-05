from django.db import models

from autoslug import AutoSlugField


class Campaign(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)

    description = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    campaign = models.ForeignKey('Campaign')
    is_pc = models.BooleanField(default=False)

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=(
            ('Alive', 'Alive'),
            ('Deceased', 'Deceased'),
            ('Unknown', 'Unknown'),
        )
    )

    description = models.CharField(max_length=5000)
    faction = models.ForeignKey('Faction', blank=True, null=True)
    location = models.ForeignKey('Location', related_name='location')
    previous_locations = models.ManyToManyField('Location', related_name='previous_locations', blank=True)

    def __str__(self) -> str:
        return self.name


class Faction(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    campaign = models.ForeignKey('Campaign')

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)

    description = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    campaign = models.ForeignKey('Campaign')

    superlocation = models.ForeignKey("self", blank=True, null=True, related_name="sublocations")

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)

    description = models.CharField(max_length=5000)


    def __str__(self) -> str:
        return self.name


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = "Log Entries"

    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')

    campaign = models.ForeignKey('Campaign')

    title = models.CharField(max_length=50, unique=True)
    date = models.DateField()

    description = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.title
