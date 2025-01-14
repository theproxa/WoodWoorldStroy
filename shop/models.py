from django.db import models

# Create your models here.


    
class Catalog(models.Model):
    image = models.ImageField(upload_to='img/kind/')
    kind = models.CharField(max_length =  64)
    product_len = models.SmallIntegerField()
    thickness = models.SmallIntegerField()
    width = models.SmallIntegerField()
    material = models.CharField(max_length = 32)
    
class Case(models.Model):
    # client = models.ForeignKey(,on_delete = models.CASCADE)
    kind = models.CharField(max_length = 64)
    product_len = models.SmallIntegerField()
    thickness = models.SmallIntegerField()
    width = models.SmallIntegerField()
    material = models.CharField(max_length = 32)
    date = models.DateTimeField()
    quantity = models.IntegerField()
    price = models.IntegerField()