# Generated by Django 4.0.5 on 2022-06-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_2_project', '0003_alter_vulnes_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnes',
            name='score',
            field=models.FloatField(verbose_name='Score'),
        ),
    ]
