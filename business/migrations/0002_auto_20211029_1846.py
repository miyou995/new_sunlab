# Generated by Django 3.2.8 on 2021-10-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='title',
        ),
        migrations.AlterField(
            model_name='slide',
            name='url',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien'),
        ),
    ]
