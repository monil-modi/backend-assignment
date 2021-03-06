# Generated by Django 2.1.15 on 2021-03-08 15:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='light',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='thermostat',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False),
        ),
    ]
