# Generated by Django 3.2.6 on 2021-09-30 19:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210930_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='intro_paragraph_1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='intro_paragraph_2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]