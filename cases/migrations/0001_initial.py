# Generated by Django 3.0.5 on 2020-05-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covidcasesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('total_cases', models.IntegerField(blank=True, default=0)),
                ('current_cases', models.IntegerField(blank=True, default=0)),
                ('death_cases', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]