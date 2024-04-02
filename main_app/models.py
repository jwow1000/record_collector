from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}, {self.release_date}'


    