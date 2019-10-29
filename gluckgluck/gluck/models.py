from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(default="new page", max_length=300)
    
    def __str__(self):
        return self.title

#class Section(models.Model):
#    page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)
#    section_title = models.TextField(null=False, max_length=200)
#    def __str__(self):
#        return self.section_title

class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)
    section_title = models.CharField(blank=True, null=True, max_length=200)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        text = ""
        if self.section_title:
            text+="title "
        if self.text:
             text+="text "
        if self.image:
             text+="image " 
        return text
    
    class Meta:
        verbose_name = "Component"



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
    

