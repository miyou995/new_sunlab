# Generated by Django 3.2.8 on 2021-10-30 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211030_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='is_active',
            new_name='actif',
        ),
    ]