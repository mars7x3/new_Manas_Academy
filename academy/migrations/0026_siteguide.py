# Generated by Django 4.1 on 2022-09-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0025_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='management-images', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Наводка по сайту',
                'verbose_name_plural': 'Наводка по сайту',
            },
        ),
    ]
