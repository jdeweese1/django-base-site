# Generated by Django 2.1.2 on 2018-11-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='sender_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
