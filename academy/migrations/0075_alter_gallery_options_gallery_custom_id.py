# Generated by Django 4.1.6 on 2023-02-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0074_socialmedia_twitter_socialmedia_vk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ('custom_id',), 'verbose_name': 'Галерея - Авторы', 'verbose_name_plural': 'Галерея - Авторы'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='custom_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID'),
        ),
    ]
