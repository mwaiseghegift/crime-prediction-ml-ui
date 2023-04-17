# Generated by Django 4.1 on 2023-04-13 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('case_number', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('block', models.CharField(max_length=50)),
                ('iucr', models.CharField(max_length=10)),
                ('primary_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('location_description', models.CharField(max_length=100)),
                ('arrest', models.BooleanField()),
                ('domestic', models.BooleanField()),
                ('beat', models.IntegerField()),
                ('district', models.IntegerField()),
                ('ward', models.FloatField(blank=True, null=True)),
                ('community_area', models.IntegerField()),
                ('fbi_code', models.CharField(max_length=10)),
                ('x_coordinate', models.FloatField(blank=True, null=True)),
                ('y_coordinate', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('updated_on', models.DateTimeField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Crime Records',
                'db_table': 'crime_records',
                'ordering': ('date',),
                'managed': True,
            },
        ),
    ]