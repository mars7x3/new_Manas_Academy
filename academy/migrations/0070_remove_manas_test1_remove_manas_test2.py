# Generated by Django 4.1 on 2022-09-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0069_manasfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manas',
            name='test1',
        ),
        migrations.RemoveField(
            model_name='manas',
            name='test2',
        ),
    ]
