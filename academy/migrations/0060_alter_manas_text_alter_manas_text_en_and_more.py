# Generated by Django 4.1 on 2022-09-09 07:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0059_remove_news_tag_en_remove_news_tag_ky_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manas',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AlterField(
            model_name='manas',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AlterField(
            model_name='manas',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AlterField(
            model_name='manas',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
    ]
