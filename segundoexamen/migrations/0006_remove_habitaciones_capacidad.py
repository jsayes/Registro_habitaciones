# Generated by Django 4.2.1 on 2023-05-07 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segundoexamen', '0005_remove_habitaciones_numero_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitaciones',
            name='capacidad',
        ),
    ]
