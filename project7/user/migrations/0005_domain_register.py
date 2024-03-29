# Generated by Django 4.0.7 on 2022-12-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='domain_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('purpose', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('type', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
