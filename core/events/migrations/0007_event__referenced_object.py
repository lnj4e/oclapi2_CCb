# Generated by Django 4.2.11 on 2024-08-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='_referenced_object',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
