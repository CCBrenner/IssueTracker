# Generated by Django 3.2.2 on 2021-07-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='deleted_status',
            field=models.BooleanField(default=False),
        ),
    ]
