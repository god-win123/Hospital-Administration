from django.db import models

# Create your models here.
class Hospital_table(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Images = models.ImageField(upload_to='new_pic')
    def __str__(self):
        return self.name
