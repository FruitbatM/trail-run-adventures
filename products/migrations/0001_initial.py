# Generated by Django 3.2.6 on 2021-09-17 17:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'itineraries',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=80)),
                ('holiday_header_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('header_paragraph', models.TextField(max_length=800)),
                ('duration', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('distance', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(200)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('single_supplement', models.BooleanField(default=False)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('number_of_runners', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(14)])),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(76)])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('guide', models.CharField(max_length=80)),
                ('overview_paragraph_1', models.TextField(max_length=500)),
                ('overview_paragraph_2', models.TextField(max_length=800)),
                ('overview_paragraph_3', models.TextField(max_length=800)),
                ('running_days', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('min_elavation', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3000)])),
                ('max_elavation', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)])),
                ('elevation_gain', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(12000)])),
                ('is_holiday', models.BooleanField(default=False)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('route_image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(max_length=800)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.level')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_1', models.CharField(max_length=254, null=True)),
                ('day_1_overview', models.TextField(max_length=800)),
                ('day_1_data', models.TextField(max_length=400)),
                ('day_2', models.CharField(max_length=254, null=True)),
                ('day_2_overview', models.TextField(max_length=800)),
                ('day_2_data', models.TextField(max_length=400)),
                ('day_3', models.CharField(max_length=254, null=True)),
                ('day_3_overview', models.TextField(max_length=800)),
                ('day_3_data', models.TextField(max_length=400)),
                ('day_4', models.CharField(max_length=254, null=True)),
                ('day_4_overview', models.TextField(max_length=800)),
                ('day_4_data', models.TextField(max_length=400)),
                ('day_5', models.CharField(max_length=254, null=True)),
                ('day_5_overview', models.TextField(max_length=800)),
                ('day_5_data', models.TextField(max_length=400)),
                ('day_6', models.CharField(max_length=254, null=True)),
                ('day_6_overview', models.TextField(max_length=800)),
                ('day_6_data', models.TextField(max_length=400)),
                ('day_7', models.CharField(max_length=254, null=True)),
                ('day_7_overview', models.TextField(max_length=800)),
                ('day_7_data', models.TextField(max_length=400)),
                ('day_8', models.CharField(max_length=254, null=True)),
                ('day_8_overview', models.TextField(max_length=800)),
                ('day_8_data', models.TextField(max_length=400)),
                ('itinerary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.itinerary')),
            ],
        ),
        migrations.AddField(
            model_name='itinerary',
            name='holiday',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
