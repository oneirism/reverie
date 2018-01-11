from django.db import models

from .utils import get_unique_slug


class Campaign(models.Model):
    slug = models.SlugField(max_length=140, unique=True)

    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField(max_length=100)

    description = models.CharField(max_length=5000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save()

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    slug = models.SlugField(max_length=140, unique=True)

    campaign = models.ForeignKey('Campaign', models.CASCADE)
    is_pc = models.BooleanField(default=False)

    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)
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
    faction = models.ForeignKey('Faction', models.CASCADE, blank=True, null=True)
    location = models.ForeignKey('Location', models.CASCADE, related_name='location')
    previous_locations = models.ManyToManyField('Location', related_name='previous_locations', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save()

    def __str__(self) -> str:
        return self.name


class Faction(models.Model):
    slug = models.SlugField(max_length=140, unique=True)

    campaign = models.ForeignKey('Campaign', models.CASCADE)

    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)

    description = models.CharField(max_length=5000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save()

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    slug = models.SlugField(max_length=140, unique=True)

    campaign = models.ForeignKey('Campaign', models.CASCADE)

    superlocation = models.ForeignKey("self", models.CASCADE, blank=True, null=True, related_name="sublocations")

    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)

    description = models.CharField(max_length=5000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save()

    def __str__(self) -> str:
        return self.name


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = "Log Entries"

    slug = models.SlugField(max_length=140, unique=True)

    campaign = models.ForeignKey('Campaign', models.CASCADE)

    title = models.CharField(max_length=50)
    date = models.DateField()

    description = models.CharField(max_length=5000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self) -> str:
        return self.title
