from django.db import models

# Create your models here.
class Url(models.Model) :
    mainUrl = models.CharField(max_length=100)
