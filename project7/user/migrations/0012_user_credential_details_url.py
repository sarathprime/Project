# Generated by Django 4.0.7 on 2022-12-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_user_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_credential_details',
            name='url',
            field=models.CharField(default='exir', max_length=150),
            preserve_default=False,
        ),
    ]