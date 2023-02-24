# Generated by Django 4.0.1 on 2023-02-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appnetfloox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('primaryName', models.CharField(max_length=100)),
                ('primaryTitle', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=100)),
                ('startYear', models.FloatField()),
            ],
        ),
    ]
