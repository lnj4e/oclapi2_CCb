# Generated by Django 3.2.8 on 2021-11-29 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0026_merge_0020_auto_20210811_1058_0025_mapping__counted'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='mapping',
            name='mappings_is_acti_ccfa00_idx',
        ),
    ]
