# Generated by Django 3.2.6 on 2021-09-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210918_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='guide',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='header_paragraph',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='overview_paragraph_1',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='overview_paragraph_2',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='overview_paragraph_3',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]