# Generated by Django 3.2.6 on 2021-09-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
