from django.db import models
# from django import forms
# import datetime
# Create your models here.


class Transaction(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    deb_amt = models.IntegerField()
    cr_amt = models.IntegerField()
    acc_bal = models.IntegerField()


class User(models.Model):
    img = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    country = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length=30)
    balance = models.IntegerField()


class TransactionsForm(models.Model):
    sender = models.EmailField(max_length=40)
    amount = models.IntegerField()
    receiver = models.EmailField(max_length=40)






