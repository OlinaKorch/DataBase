# Generated by Django 3.2.7 on 2023-02-28 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20230228_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectimage',
            name='object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.objects'),
        ),
    ]
