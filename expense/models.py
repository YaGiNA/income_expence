from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    pub_date = models.DateTimeField('date of paid')

    def __str__(self):
        return self.title

    def was_paid_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)