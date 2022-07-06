# Generated by Django 4.0.4 on 2022-07-06 02:23

from django.db import migrations

from core.collections.parsers import CollectionReferenceExpressionStringParser
from core.common.utils import to_parent_uri, drop_version, separate_version


def populate_reference_system_and_valueset(apps, schema_editor):
    CollectionReference = apps.get_model('collections', 'CollectionReference')
    for reference in CollectionReference.objects.filter(
            expression__isnull=False, system__isnull=True, valueset__isnull=True):
        parser = CollectionReferenceExpressionStringParser(expression=reference.expression)
        parser.parse()
        ref_struct = parser.to_reference_structure()[0]
        reference.reference_type = ref_struct['reference_type']
        reference.system = ref_struct['system']
        reference.version = ref_struct['version']
        reference.code = ref_struct['code']
        reference.resource_version = ref_struct['resource_version']
        reference.valueset = ref_struct['valueset']
        reference.filter = ref_struct['filter']
        reference.save()


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0053_alter_collection_canonical_url'),
    ]

    operations = [
        migrations.RunPython(populate_reference_system_and_valueset)
    ]
