# Generated by Django 4.2.7 on 2024-02-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]
