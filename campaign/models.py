""" Reverie campaign model definitions. """
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from image_cropping import ImageRatioField

from .helpers import RandomFileName
from reverie.utils import markdownify

# Create your models here.
class Campaign(models.Model):
    """ A Reverie campaign. """
    slug = models.SlugField(
        unique=True,
    )

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        max_length=50,
    )

    image = models.ImageField(
        blank=True,
        upload_to=RandomFileName('images/campaign')
    )

    cropping = ImageRatioField('image', '1500x500')

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

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        # FIXME(devenney): Kind of smells, but users hardcode slugs in their MD
        #                  cross-references so this can't change.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Campaign, self).save(*args, **kwargs)


class Character(models.Model):
    """ A Reverie campaign character. """
    slug = models.SlugField(
        blank=True,
        unique=True
    )

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    is_pc = models.BooleanField(
        default=False,
    )

    tagline = models.CharField(
        max_length=50,
    )

    image = models.ImageField(
        blank=True,
        upload_to='uploaded_images'
    )

    cropping = ImageRatioField('image', '500x500')

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

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        # FIXME(devenney): Kind of smells, but users hardcode slugs in their MD
        #                  cross-references so this can't change.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Character, self).save(*args, **kwargs)


class Faction(models.Model):
    """ A Reverie campaign faction. """
    slug = models.SlugField(
        unique=True
    )

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        max_length=50,
    )

    image = models.ImageField(
        blank=True,
        upload_to='uploaded_images'
    )

    cropping = ImageRatioField('image', '500x500')

    description = models.TextField(
        max_length=500,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        # FIXME(devenney): Kind of smells, but users hardcode slugs in their MD
        #                  cross-references so this can't change.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Faction, self).save(*args, **kwargs)


class Item(models.Model):
    """ A Reverie campaign item. """
    slug = models.SlugField(
        unique=True
    )

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        unique=True,
        max_length=50,
    )

    image = models.ImageField(
        blank=True,
        upload_to='uploaded_images'
    )

    cropping = ImageRatioField('image', '500x500')

    description = models.TextField(
        max_length=500,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        # FIXME(devenney): Kind of smells, but users hardcode slugs in their MD
        #                  cross-references so this can't change.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)


class Location(models.Model):
    """ A Reverie campaign location. """
    slug = models.SlugField(
        unique=True
    )

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    tagline = models.CharField(
        unique=True,
        max_length=50,
    )

    image = models.ImageField(
        blank=True,
        upload_to='uploaded_images'
    )

    cropping = ImageRatioField('image', '500x500')

    description = models.TextField(
        max_length=500,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        # FIXME(devenney): Kind of smells, but users hardcode slugs in their MD
        #                  cross-references so this can't change.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)


class Log(models.Model):
    """ A Reverie campaign log entry. """
    slug = models.SlugField(
        unique=True
    )

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    image = models.ImageField(
        blank=True,
        upload_to='uploaded_images'
    )

    cropping = ImageRatioField('image', '1500x500')

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
        return self.name

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        # FIXME(devenney): Kind of smells, but users hardcode slugs in their MD
        #                  cross-references so this can't change.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Log, self).save(*args, **kwargs)
