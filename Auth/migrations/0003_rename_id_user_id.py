# Generated by Django 4.1.7 on 2023-06-23 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_remove_user_groups'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ID',
            new_name='id',
        ),
    ]
