# Generated by Django 3.2.6 on 2021-09-30 19:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210930_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content_1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
