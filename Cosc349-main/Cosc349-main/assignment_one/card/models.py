from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Card_colour(models.Model):
    name = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from=['name'])
    def __str__(self):
        return self.name

class Card_supertype(models.Model):
    name = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from=['name'])
    def __str__(self):
        return self.name
class Card_type(models.Model):
    name = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from=['name'])
    def __str__(self):
        return self.name
class Card_subtype(models.Model):
    name = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from=['name'])
    def __str__(self):
        return self.name

class Card_set(models.Model):
    code = models.CharField(max_length = 5)
    name = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from=['name'])
    def __str__(self):
        return self.code

class Card(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255)
    manaCost = models.CharField(max_length=100)
    # converted mana cost(total mana)
    cmc = models.IntegerField()
    artist = models.CharField(max_length=100)
    rarity =  models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add= True)

    # many to many fields
    superTypes =  models.ManyToManyField(Card_supertype)
    cardTypes = models.ManyToManyField(Card_type)
    subtypes = models.ManyToManyField(Card_subtype)
    colours = models.ManyToManyField(Card_colour)

    # many to one fields
    cardSet = models.ForeignKey(Card_set, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/card/{self.slug}/'