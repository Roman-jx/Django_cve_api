# Generated by Django 4.0.5 on 2022-06-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_2_project', '0002_vulnes_delete_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnes',
            name='score',
            field=models.PositiveBigIntegerField(verbose_name='Score'),
        ),
    ]
