# Generated by Django 3.2.2 on 2021-08-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
