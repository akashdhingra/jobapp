# Generated by Django 4.2.7 on 2024-02-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobpost_date_jobpost_description_jobpost_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
