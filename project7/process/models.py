from django.db import models

class process_register(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)


class process_team_id(models.Model):
    email=models.EmailField(max_length=150)