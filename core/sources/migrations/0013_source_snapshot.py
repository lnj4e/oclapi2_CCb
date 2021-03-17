# Generated by Django 3.0.9 on 2021-03-09 04:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0012_source_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='snapshot',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]