from django.db import models
from users.models import CustomUser
# Create your models here.


    
class Catalog(models.Model):
    image = models.ImageField(upload_to='img/kind/')
    kind = models.CharField(max_length =  64)
    product_len = models.SmallIntegerField()
    thickness = models.SmallIntegerField()
    width = models.SmallIntegerField()
    material = models.CharField(max_length = 32)
    
class Case(models.Model):
    client_id = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    client_phone = models.IntegerField()
    client_adress = models.CharField(max_length = 256)
    catalog_id = models.ForeignKey(Catalog, on_delete=models.PROTECT)
    kind = models.CharField(max_length = 64)
    product_len = models.SmallIntegerField()
    thickness = models.SmallIntegerField()
    width = models.SmallIntegerField()
    material = models.CharField(max_length = 32)
    date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()