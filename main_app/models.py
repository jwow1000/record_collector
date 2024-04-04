from django.db import models
from datetime import datetime

# Create your models here.


class Record(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}, {self.artist}, {self.release_date}'

class Dj(models.Model):
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # join through
    records = models.ManyToManyField(Record, through='Spin')
    def __str__(self):
        return f'{self.full_name}'

# join through table
class Spin(models.Model):
    datetime = models.DateTimeField('When this Record was Spun')
    rpm = models.FloatField()
    # join through : 
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    dj = models.ForeignKey(Dj, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.dj.full_name} spun the record {self.record.title} at {self.datetime}'

    # change the default sort
    class Meta:
        ordering = ['-datetime']
