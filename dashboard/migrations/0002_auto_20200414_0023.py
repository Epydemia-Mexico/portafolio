# Generated by Django 3.0.5 on 2020-04-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
