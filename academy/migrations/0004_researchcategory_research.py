# Generated by Django 4.1 on 2022-09-01 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_alter_homeabout_options_alter_statistic_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Категория иследования')),
            ],
            options={
                'verbose_name': 'Исследования - Категория',
                'verbose_name_plural': 'Исследования - Категория',
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название иследования')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.researchcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Исследования - Категория',
                'verbose_name_plural': 'Исследования - Категория',
            },
        ),
    ]
