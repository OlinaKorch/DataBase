# Generated by Django 3.2.7 on 2023-02-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_objects_eds_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objects',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год'),
        ),
    ]
