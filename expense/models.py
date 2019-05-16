from django.db import models

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    pub_date = models.DateTimeField('date of paid')
