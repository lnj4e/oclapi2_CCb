# Generated by Django 4.2.4 on 2024-03-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]