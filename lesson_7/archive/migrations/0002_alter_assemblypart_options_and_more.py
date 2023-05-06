# Generated by Django 4.2 on 2023-05-05 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assemblypart',
            options={'verbose_name': 'Деталь в сборке', 'verbose_name_plural': 'Детали в сборке'},
        ),
        migrations.AlterField(
            model_name='assemblypart',
            name='assembly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.assembly', verbose_name='Сборка'),
        ),
        migrations.AlterField(
            model_name='assemblypart',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archive.part', verbose_name='Деталь'),
        ),
    ]
