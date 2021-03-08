# Generated by Django 2.1.15 on 2021-03-08 16:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_auto_20210308_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightStateChangeInformation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False)),
                ('previous_state', jsonfield.fields.JSONField(default=dict)),
                ('next_state', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomStateChangeInformation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False)),
                ('previous_state', jsonfield.fields.JSONField(default=dict)),
                ('next_state', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThermostatStateChangeInformation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False)),
                ('previous_state', jsonfield.fields.JSONField(default=dict)),
                ('next_state', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='house',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updated At'),
        ),
        migrations.AddField(
            model_name='light',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='light',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updated At'),
        ),
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1, help_text='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updated At'),
        ),
        migrations.AddField(
            model_name='thermostat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=2, help_text='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thermostat',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updated At'),
        ),
        migrations.AddField(
            model_name='thermostatstatechangeinformation',
            name='thermostat',
            field=models.ForeignKey(help_text='Thermostat State Change', on_delete=django.db.models.deletion.CASCADE, related_name='thermostats', to='homes.Thermostat'),
        ),
        migrations.AddField(
            model_name='roomstatechangeinformation',
            name='room',
            field=models.ForeignKey(help_text='Room State Change', on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='homes.Room'),
        ),
        migrations.AddField(
            model_name='lightstatechangeinformation',
            name='light',
            field=models.ForeignKey(help_text='Light State Change', on_delete=django.db.models.deletion.CASCADE, related_name='lights', to='homes.Light'),
        ),
    ]