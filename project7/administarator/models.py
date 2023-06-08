from django.db import models

class domain_id_generate(models.Model):
    email=models.EmailField(max_length=150)
    id_donor = models.CharField(max_length=150)

class admin_payslip(models.Model):
    email=models.EmailField(max_length=150)
    access_id = models.CharField(max_length=150)