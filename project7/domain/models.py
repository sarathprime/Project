from django.db import models

class process_register(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)



class domain_1_access(models.Model):
    user_email=models.EmailField(max_length=150)
    purpose = models.CharField(max_length=150)


class decryption_Requst(models.Model):
    user_email=models.EmailField(max_length=150)


class decryption_Requst_2(models.Model):
    user_email=models.EmailField(max_length=150)