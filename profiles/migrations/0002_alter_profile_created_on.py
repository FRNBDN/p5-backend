# Generated by Django 4.1.5 on 2023-01-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
