from django.contrib import admin

# Register your models here.
from .models import Record, Spin, Dj

admin.site.register(Record)
admin.site.register(Spin)
admin.site.register(Dj)

