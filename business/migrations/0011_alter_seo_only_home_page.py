# Generated by Django 3.2.8 on 2021-11-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_seo_only_home_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='only_home_page',
            field=models.BooleanField(default=False, verbose_name='Page principale uniquement'),
        ),
    ]
