# Generated by Django 4.1 on 2023-04-13 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crime',
            options={'ordering': ('date',), 'verbose_name_plural': 'Crime Records'},
        ),
    ]
