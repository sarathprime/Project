# Generated by Django 4.0.7 on 2022-12-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_password_domain_purpose_register_enquiry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('organisation', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('purpose', models.CharField(max_length=150)),
                ('enquiry', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
