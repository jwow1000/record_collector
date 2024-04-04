from django.db import models
from datetime import date

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}, {self.release_date}'

class Spin(models.Model):
    date = models.DateField('When this Record was Spun')
    rpm = models.FloatField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f'spun the record {self.record.title} at {self.date}'

    