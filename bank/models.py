from django.db import models
from datetime import datetime

# Create your models here.
class Customers(models.Model):
    cust_id=models.AutoField
    cust_name=models.CharField(max_length=20)
    cust_email=models.EmailField(max_length=100)
    cust_balance=models.IntegerField()

    def __str__(self):
        return self.cust_name

class Transfer(models.Model):
    sender=models.IntegerField()
    receiver=models.IntegerField()
    bal=models.IntegerField()
    comment=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"""{self.sender} -> {self.receiver}"""