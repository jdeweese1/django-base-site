# Generated by Django 2.1.4 on 2019-01-07 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20181127_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]