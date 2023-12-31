# Generated by Django 4.1.7 on 2023-06-16 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datatype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=500, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('datatype_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Form.datatype')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('department_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.department')),
                ('field_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Form.formfield')),
                ('service_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]
