# Generated by Django 4.1.3 on 2023-01-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_rename_hore_cita_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Descripción'),
        ),
    ]