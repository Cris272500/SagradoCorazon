# Generated by Django 5.0.6 on 2024-11-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
