from django.db import models

# Create your models here.

class Destination(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Balance = models.IntegerField()

    # for Trnsfer
class Transfer(models.Model):
    sender = models.CharField(max_length=200, null=True)
    reciever = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(default=0)
    date_tran = models.DateTimeField(auto_now_add=True)