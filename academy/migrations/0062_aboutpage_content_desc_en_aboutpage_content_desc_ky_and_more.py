# Generated by Django 4.1 on 2022-09-09 07:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0061_manas_tag_en_manas_tag_ky_manas_tag_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='content_desc_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание направления'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_desc_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание направления'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_desc_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание направления'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название направления'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название направления'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название направления'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='department_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Отделы'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='department_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Отделы'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='department_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Отделы'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание Академии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='description_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание Академии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание Академии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_desc_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание миссии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_desc_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание миссии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_desc_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание миссии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Миссия'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Миссия'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Миссия'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='tasks_desc_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание задачи'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='tasks_desc_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание задачи'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='tasks_desc_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание задачи'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='tasks_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название задачи'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='tasks_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название задачи'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='tasks_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название задачи'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название Академии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название Академии'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название Академии'),
        ),
        migrations.AddField(
            model_name='archive',
            name='tag_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='tag_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='tag_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Название архива'),
        ),
        migrations.AddField(
            model_name='archive',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название архива'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='date_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Дата жизни'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='date_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Дата жизни'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='date_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Дата жизни'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='title_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Название картины'),
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='title_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Название картины'),
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Название картины'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='big_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Большое название'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='big_title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Большое название'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='big_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Большое название'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание академии'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='description_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание академии'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание академии'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='small_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Маленькое название'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='small_title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Маленькое название'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='small_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Маленькое название'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название академии'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название академии'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название академии'),
        ),
        migrations.AddField(
            model_name='logo',
            name='logo_en',
            field=models.ImageField(null=True, upload_to='logotype', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='logo',
            name='logo_ky',
            field=models.ImageField(null=True, upload_to='logotype', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='logo',
            name='logo_ru',
            field=models.ImageField(null=True, upload_to='logotype', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='management',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='management',
            name='name_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='management',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='management',
            name='position_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='management',
            name='position_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='management',
            name='position_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='news',
            name='tag_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='tag_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='tag_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Название новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название новости'),
        ),
        migrations.AddField(
            model_name='npa',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание НПА'),
        ),
        migrations.AddField(
            model_name='npa',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание НПА'),
        ),
        migrations.AddField(
            model_name='npa',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание НПА'),
        ),
        migrations.AddField(
            model_name='onlinemagazine',
            name='button_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название кнопки'),
        ),
        migrations.AddField(
            model_name='onlinemagazine',
            name='button_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название кнопки'),
        ),
        migrations.AddField(
            model_name='onlinemagazine',
            name='button_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название кнопки'),
        ),
        migrations.AddField(
            model_name='project',
            name='tag_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='tag_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='tag_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Тег проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='research',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание исследования'),
        ),
        migrations.AddField(
            model_name='research',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание исследования'),
        ),
        migrations.AddField(
            model_name='research',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание исследования'),
        ),
        migrations.AddField(
            model_name='research',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название иследования'),
        ),
        migrations.AddField(
            model_name='research',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Название иследования'),
        ),
        migrations.AddField(
            model_name='research',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название иследования'),
        ),
        migrations.AddField(
            model_name='researchcategory',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Категория иследования'),
        ),
        migrations.AddField(
            model_name='researchcategory',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Категория иследования'),
        ),
        migrations.AddField(
            model_name='researchcategory',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Категория иследования'),
        ),
        migrations.AddField(
            model_name='siteguide',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='siteguide',
            name='title_ky',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='siteguide',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='telegram_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='telegram_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='telegram_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название статистики'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название статистики'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название статистики'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название направления'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание направления'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='department',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Отделы'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание Академии'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='mission',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Миссия'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='mission_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание миссии'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='tasks',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название задачи'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='tasks_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание задачи'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='title',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Название Академии'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание архива'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='homeabout',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание академии'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание новости'),
        ),
        migrations.AlterField(
            model_name='npa',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание НПА'),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание проекта'),
        ),
        migrations.AlterField(
            model_name='research',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание исследования'),
        ),
    ]
