# Generated by Django 3.2.6 on 2021-10-02 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_faq_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='holiday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
