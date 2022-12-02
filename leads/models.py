from django.db import models


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


class Agent(models.Model):
    affiliate_id = models.CharField(max_length=10)
    affiliate_name = models.CharField(max_length=20)
    parent_company = models.CharField(max_length=20)
    staff_ids = models.CharField(max_length=100)
    affiliate_country = models.CharField(max_length=20)
    affiliate_city = models.CharField(max_length=20)
    affiliate_location = models.CharField(max_length=50)
    affiliate_percent = models.CharField(max_length=2)
    phone1 = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    contact_id = models.CharField(max_length=10)
    reg_date = models.CharField(max_length=20)