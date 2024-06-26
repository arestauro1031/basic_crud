# Generated by Django 5.0.4 on 2024-04-15 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('positionID', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empID', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobileno', models.CharField(max_length=50)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.position')),
            ],
        ),
    ]
