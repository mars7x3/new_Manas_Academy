# Generated by Django 4.1 on 2022-09-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0040_research_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание проекта'),
        ),
    ]
