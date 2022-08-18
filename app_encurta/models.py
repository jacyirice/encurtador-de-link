from django.db import models

# Create your models here.
class Link(models.Model):
    link = models.URLField("Link", max_length=255)
    link_short = models.CharField("Link short", max_length=200, unique=True)
    