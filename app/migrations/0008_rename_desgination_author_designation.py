# Generated by Django 4.2.7 on 2024-02-18 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_author_jobpost_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='desgination',
            new_name='designation',
        ),
    ]
