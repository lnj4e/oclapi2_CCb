# Generated by Django 3.2.8 on 2021-11-29 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0026_merge_0018_auto_20210804_0957_0025_concept__counted'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_is_acti_7190c6_idx',
        ),
    ]
