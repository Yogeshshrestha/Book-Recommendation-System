# Generated by Django 4.0.2 on 2022-04-25 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_checkout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='checkout',
        ),
    ]