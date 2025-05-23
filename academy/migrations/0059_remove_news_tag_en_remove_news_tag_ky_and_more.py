# Generated by Django 4.1 on 2022-09-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0058_alter_manas_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tag_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='tag_ky',
        ),
        migrations.RemoveField(
            model_name='news',
            name='tag_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text_ky',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ky',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
        migrations.AddField(
            model_name='manas',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AddField(
            model_name='manas',
            name='text_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AddField(
            model_name='manas',
            name='text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AlterField(
            model_name='manas',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
    ]
