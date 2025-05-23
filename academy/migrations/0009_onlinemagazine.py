# Generated by Django 4.1 on 2022-09-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_project_date_project_tag_alter_project_banner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineMagazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='magazine-image', verbose_name='Банер')),
                ('image', models.ImageField(blank=True, null=True, upload_to='magazine-image', verbose_name='Фото журнала')),
                ('button', models.ImageField(blank=True, null=True, upload_to='magazine-image', verbose_name='Название кнопки')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журнал',
            },
        ),
    ]
