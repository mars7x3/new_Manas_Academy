# Generated by Django 4.1 on 2022-09-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0027_siteguide_link_alter_siteguide_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteguide',
            name='link_oder',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка URL'),
        ),
        migrations.AlterField(
            model_name='siteguide',
            name='link',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ссылка'),
        ),
    ]
