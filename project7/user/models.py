from django.db import models

class user_register(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)


class domain_register(models.Model):
    name=models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    type = models.CharField(max_length=150)
    password = models.CharField(max_length=150, null=True)



class domain_purpose_register(models.Model):
    name=models.CharField(max_length=150)
    organisation = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    purpose = models.CharField(max_length=150)
    enquiry = models.CharField(max_length=150, null=True)
    boo3 = models.BooleanField(default=False)


class user_detail(models.Model):
    name=models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    address = models.CharField(max_length=150)
    enquiry = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=150)
    boo2=models.BooleanField(default=False)


class user_credential_details(models.Model):
    username=models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150, null=True)
    predict = models.CharField(max_length=150)
    pincode = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    url= models.CharField(max_length=150)
    file = models.ImageField(upload_to='documents')
    bollean=models.BooleanField(default=False)
