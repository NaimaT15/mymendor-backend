# Generated by Django 4.1.7 on 2023-06-22 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_service_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='dep_ID',
        ),
    ]
