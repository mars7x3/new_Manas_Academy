# Generated by Django 4.1 on 2022-09-04 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0045_gallery_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название картины')),
                ('image', models.ImageField(upload_to='gallery-images', verbose_name='Картина')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_images', to='academy.gallery', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Галерея - Картины',
                'verbose_name_plural': 'Галерея - Картины',
            },
        ),
    ]
