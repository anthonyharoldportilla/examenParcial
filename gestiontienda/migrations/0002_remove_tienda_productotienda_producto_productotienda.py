# Generated by Django 4.2.3 on 2023-08-06 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestiontienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='productoTienda',
        ),
        migrations.AddField(
            model_name='producto',
            name='productoTienda',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiontienda.tienda'),
        ),
    ]
