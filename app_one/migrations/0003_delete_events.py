# Generated by Django 3.0.8 on 2020-07-30 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_remove_events_posted_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Events',
        ),
    ]