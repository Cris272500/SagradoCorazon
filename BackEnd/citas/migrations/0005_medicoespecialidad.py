# Generated by Django 5.0.6 on 2024-11-15 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0004_especialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicoEspecialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.especialidad')),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.medico')),
            ],
            options={
                'unique_together': {('id_medico', 'id_especialidad')},
            },
        ),
    ]