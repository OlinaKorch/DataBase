# Generated by Django 3.2.7 on 2023-02-28 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_objectimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectimage',
            name='default',
        ),
        migrations.RemoveField(
            model_name='objectimage',
            name='name',
        ),
    ]
