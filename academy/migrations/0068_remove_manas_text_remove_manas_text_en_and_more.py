# Generated by Django 4.1 on 2022-09-10 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0067_alter_manas_text_alter_manas_text_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manas',
            name='text',
        ),
        migrations.RemoveField(
            model_name='manas',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='manas',
            name='text_ky',
        ),
        migrations.RemoveField(
            model_name='manas',
            name='text_ru',
        ),
    ]
