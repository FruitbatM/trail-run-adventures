# Generated by Django 3.2.6 on 2021-09-17 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_itinerary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryDay',
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
    ]
