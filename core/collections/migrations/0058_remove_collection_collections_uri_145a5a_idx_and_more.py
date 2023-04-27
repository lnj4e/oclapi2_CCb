# Generated by Django 4.1.7 on 2023-04-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0057_alter_collection_custom_validation_schema'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='collection',
            name='collections_uri_145a5a_idx',
        ),
        migrations.AlterField(
            model_name='collection',
            name='uri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expansion',
            name='uri',
            field=models.TextField(blank=True, null=True),
        ),
    ]