from django.db import models

# Create your models here.

class Category(models.Model):
	category=models.CharField(max_length=50)
	def __str__(self):
		return self.category		

class Item(models.Model):
	item_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	def __str__(self):
		return self.name



