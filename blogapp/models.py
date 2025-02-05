from django.db import models

# Create your models here.
class Blogs(models.Model):
    Blog_ID =models.CharField(max_length=10)
    BlogTitle = models.CharField(max_length=50)
    Description = models.CharField(max_length=5000)
    Author=models.CharField(max_length=100)
    Date=models.CharField(max_length=25)
    class meta:
        db_table='Blog_Table'
        