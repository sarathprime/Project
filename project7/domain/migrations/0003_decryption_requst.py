# Generated by Django 4.0.7 on 2022-12-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0002_domain_1_access'),
    ]

    operations = [
        migrations.CreateModel(
            name='decryption_Requst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=150)),
            ],
        ),
    ]
