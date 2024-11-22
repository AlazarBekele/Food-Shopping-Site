from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Category (models.Model):

    title = models.CharField (max_length=30)

    def __str__(self):
        return self.title
    
class Index (models.Model):

    Image = models.ImageField (upload_to='Photo/')
    Title = models.CharField (max_length=30)
    Price = models.IntegerField ()
    Description = models.CharField (max_length=30)
    Rating = models.IntegerField (validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.Title

class Index_page_image (models.Model):

    Title = models.CharField (max_length=50)
    Picture = models.ImageField (upload_to='indexImg/')

    def __str__(self):
        return self.Title
    

class x_icon_Dynamic (models.Model):

    Title = models.CharField (max_length=30)
    icon = models.ImageField (upload_to='X-icon/')

    def __str__(self):
        return self.Title