# Generated by Django 4.1.5 on 2023-03-01 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='estacion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='incidencias.estaciones'),
        ),
    ]