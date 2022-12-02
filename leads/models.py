from django.db import models

# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # agent = models.ForeignKey("", on_delete=models.CASCADE)

class Worker(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teudat_zeut = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    vip = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=10)
    reg_date = models.CharField(max_length=10)
    age = models.IntegerField(default=0)