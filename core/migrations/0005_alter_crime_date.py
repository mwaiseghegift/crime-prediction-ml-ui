# Generated by Django 4.1 on 2023-04-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_crime_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
