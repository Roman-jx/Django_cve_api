# Generated by Django 4.0.5 on 2022-06-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_2_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vuln', models.CharField(max_length=255, verbose_name='Vuln ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('score', models.PositiveIntegerField(verbose_name='Score')),
            ],
            options={
                'verbose_name_plural': 'vuln',
            },
        ),
        migrations.DeleteModel(
            name='Prices',
        ),
    ]
