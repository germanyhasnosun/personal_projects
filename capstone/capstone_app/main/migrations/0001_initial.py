# Generated by Django 3.1.4 on 2021-05-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meta_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.CharField(max_length=50)),
                ('outcome_integer', models.IntegerField()),
                ('age', models.CharField(max_length=50)),
                ('age_integer', models.IntegerField()),
                ('sex', models.CharField(max_length=50)),
                ('sex_integer', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('location_integer', models.IntegerField()),
            ],
        ),
    ]
