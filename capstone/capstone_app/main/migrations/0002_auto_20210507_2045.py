# Generated by Django 3.1.4 on 2021-05-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta_data',
            name='age_integer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='meta_data',
            name='location_integer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='meta_data',
            name='outcome_integer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='meta_data',
            name='sex_integer',
            field=models.IntegerField(default=None),
        ),
    ]
