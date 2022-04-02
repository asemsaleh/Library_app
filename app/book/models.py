from django.db import models
from django import forms

# Create your models here.
from django.db import models

# Create book table 
import datetime

year_dropdown = []
for y in range(1950, (datetime.datetime.now().year + 5)):
    year_dropdown.append((y, y))

#DataFlair Models
class Book(models.Model):
    # Store necessary fields
    name = models.CharField(max_length = 50)
    #picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    year = models.IntegerField(('year'), max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)

    #email = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name