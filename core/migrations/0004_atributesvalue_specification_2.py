# Generated by Django 3.2.8 on 2021-10-30 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_is_active_producttype_actif'),
    ]

    operations = [
        migrations.AddField(
            model_name='atributesvalue',
            name='specification_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='second_values', to='core.atribute'),
        ),
    ]
