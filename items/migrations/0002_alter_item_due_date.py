# Generated by Django 4.1.5 on 2023-01-17 17:06

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='due_date',
            field=models.DateField(default=items.models.tomorrow),
        ),
    ]
