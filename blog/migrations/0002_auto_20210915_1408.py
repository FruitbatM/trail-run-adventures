# Generated by Django 3.2.6 on 2021-09-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]