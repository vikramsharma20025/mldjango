from django.db import models

# Create your models here.
class Faces(models.Model):
    phototostore = models.ImageField(upload_to='faces')