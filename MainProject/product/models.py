from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20)

class product_type(models.Model):
    type_id = models.IntegerField(models.AutoField,primary_key=True)
    type_name = models.CharField(max_length=20)
    Description = models.TextField(verbose_name='desc')
