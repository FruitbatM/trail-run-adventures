# Generated by Django 3.2.6 on 2021-09-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='about',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]