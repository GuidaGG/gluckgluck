from django.db import models
from django.utils import timezone


# Create your models here.
class Page(models.Model):
    title = models.CharField(default="new page", max_length=300)
    
    def __str__(self):
        return self.title

class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)
    section_title = models.TextField(null=False)
    def __str__(self):
        return self.section_title

class Component(models.Model):
    page = models.ForeignKey(Section, on_delete=models.CASCADE, default=None)
    text = models.TextField(null=False)
    def __str__(self):
        return self.text


class Event(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    price = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    published_date = timezone.now()
    
    def is_active(self):
        if self.date  < timezone.now():
            return True
        else:
            return False  

    def __str__(self):
        return self.title
    

