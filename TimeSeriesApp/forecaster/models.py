from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='datasets/images/', blank=True, null=True)
    file = models.FileField(upload_to='datasets/files/', blank=True, null=True)

    def __str__(self):
        return self.name
