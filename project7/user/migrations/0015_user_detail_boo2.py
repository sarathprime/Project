# Generated by Django 4.0.7 on 2022-12-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_user_credential_details_bollean'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='boo2',
            field=models.BooleanField(default=False),
        ),
    ]
