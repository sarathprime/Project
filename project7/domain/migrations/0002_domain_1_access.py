# Generated by Django 4.0.7 on 2022-12-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='domain_1_access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=150)),
                ('purpose', models.CharField(max_length=150)),
            ],
        ),
    ]
