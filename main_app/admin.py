from django.contrib import admin

# Register your models here.
from .models import Record, Spin

admin.site.register(Record)
admin.site.register(Spin)
