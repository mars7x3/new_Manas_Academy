# Generated by Django 4.1 on 2022-09-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0042_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='npabanner',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание НПА'),
        ),
    ]
