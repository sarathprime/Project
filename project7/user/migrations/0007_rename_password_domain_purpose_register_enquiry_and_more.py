# Generated by Django 4.0.7 on 2022-12-07 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_domain_purpose_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain_purpose_register',
            old_name='password',
            new_name='enquiry',
        ),
        migrations.RenameField(
            model_name='domain_purpose_register',
            old_name='type',
            new_name='organisation',
        ),
    ]