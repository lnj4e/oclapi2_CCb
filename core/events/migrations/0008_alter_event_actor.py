# Generated by Django 4.2.11 on 2024-09-02 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0007_event__referenced_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='actor_events', to=settings.AUTH_USER_MODEL),
        ),
    ]