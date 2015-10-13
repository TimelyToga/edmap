from django.db import models
from django.db.models import CharField, DateField, DateTimeField, ForeignKey
# Create your models here.

class Genre(models.Model):
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

    key = models.CharField(primary_key=True, max_length=256)
    created = DateTimeField(auto_now=True)
    name = CharField(max_length=256, unique=True)
    description = CharField(max_length=512)

class Example(models.Model):
    ## Provide an URL for an example of a certain genre
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.url

    key = models.CharField(primary_key=True, max_length=256)
    owner = ForeignKey(Genre)
    created = DateTimeField(auto_now=True)
    url = CharField(max_length=256)

class Influencer(models.Model):
    ## Influencer --> Influencee
    ## Rock influenced Pop
    #### Rock --> Pop

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.url

    key = models.CharField(primary_key=True, auto_created=True, max_length=256)
    influencer = ForeignKey(Genre)
    influencee = ForeignKey(Genre)
