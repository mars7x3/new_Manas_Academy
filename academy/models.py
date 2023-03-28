from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Statistic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики')
    statistic = models.CharField(max_length=100, verbose_name='Статистика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная - Статистика'
        verbose_name = 'Главная - Статистика'


class HomeAbout(models.Model):
    small_title = models.CharField(max_length=100, verbose_name='Маленькое название')
    big_title = models.CharField(max_length=100, verbose_name='Большое название')
    title = models.CharField(max_length=100, verbose_name='Название академии')
    description = RichTextField(verbose_name='Описание академии', blank=True, null=True)

    def __str__(self):
        return 'Раздел "О нас" на главной странице'

    class Meta:
        verbose_name_plural = 'Главная - О нас'
        verbose_name = 'Главная - О нас'


class ResearchCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория иследования')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Исследования - Категория'
        verbose_name = 'Исследования - Категория'


class Research(models.Model):
    category = models.ForeignKey(ResearchCategory, on_delete=models.DO_NOTHING, verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название иследования')
    image = models.ImageField(upload_to='research-images', verbose_name='Изображение на показ')
    banner = models.ImageField(upload_to='research-banner', blank=True, null=True, verbose_name='Банер')
    text = RichTextField(blank=True, null=True, verbose_name='Содержание исследования')

    def __str__(self):
        return f'{self.category} - {self.title}'

    class Meta:
        verbose_name_plural = 'Исследования - Иследование'
        verbose_name = 'Исследования - Иследование'


class ResearchBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Исследования"')

    def __str__(self):
        return 'Банер "Исследования"'

    class Meta:
        verbose_name_plural = 'Исследования - банер'
        verbose_name = 'Исследования - банер'


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания проекта')
    tag = models.CharField(max_length=200, blank=True, null=True, verbose_name='Тег проекта')
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')
    text = RichTextField(blank=True, null=True, verbose_name='Содержание проекта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проекты'


class ProjectBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Проекты"')

    def __str__(self):
        return 'Банер "Проекты"'

    class Meta:
        verbose_name_plural = 'Проекты - банер'
        verbose_name = 'Проекты - банер'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания новости')
    tag = models.CharField(max_length=200, blank=True, null=True, verbose_name='Тег новости')
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')
    text = RichTextField(blank=True, null=True, verbose_name='Содержание новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новости'
	

class NewsBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Новости"')

    def __str__(self):
        return 'Банер "Новости"'

    class Meta:
        verbose_name_plural = 'Новости - банер'
        verbose_name = 'Новости - банер'


class OnlineMagazine(models.Model):
    banner = models.ImageField(upload_to='magazine-image', blank=True, null=True, verbose_name='Банер')
    image = models.ImageField(upload_to='magazine-image', blank=True, null=True, verbose_name='Фото журнала')
    button = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название кнопки')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка кнопки')

    def __str__(self):
        return 'Онлайн журнал'

    class Meta:
        verbose_name_plural = 'Журнал'
        verbose_name = 'Журнал'


class Partner(models.Model):
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Логотип партнера')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка на сайт партнера')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = 'Партнёры'
        verbose_name = 'Партнёры'


class AboutPage(models.Model):
    image = models.ImageField(upload_to='about-image', blank=True, null=True, verbose_name='Фото о нас')
    title = RichTextField(blank=True, null=True, verbose_name='Название Академии')
    description = RichTextField(blank=True, null=True, verbose_name='Описание Академии')
    content = RichTextField(blank=True, null=True, verbose_name='Название направления')
    content_desc = RichTextField(blank=True, null=True, verbose_name='Описание направления')
    tasks = RichTextField(blank=True, null=True, verbose_name='Название задачи')
    tasks_desc = RichTextField(blank=True, null=True, verbose_name='Описание задачи')
    mission = RichTextField(blank=True, null=True, verbose_name='Миссия')
    mission_desc = RichTextField(blank=True, null=True, verbose_name='Описание миссии')
    department = RichTextField(blank=True, null=True, verbose_name='Отделы')

    def __str__(self):
        return 'О нас'

    class Meta:
        verbose_name_plural = 'О нас'
        verbose_name = 'О нас'


class AboutBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "О нас"')

    def __str__(self):
        return 'Банер "О нас"'

    class Meta:
        verbose_name_plural = 'О нас - банер'
        verbose_name = 'О нас - банер'


class Gallery(models.Model):
    custom_id = models.IntegerField(blank=True, null=True, verbose_name='ID')
    title = models.CharField(max_length=200, verbose_name='Имя автора')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата жизни')
    image = models.ImageField(upload_to='gallery-images', verbose_name='Фото автора')
    text = RichTextField(blank=True, null=True, verbose_name='Биография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Галерея - Авторы'
        verbose_name = 'Галерея - Авторы'
        ordering = ('custom_id', )


class GalleryImages(models.Model):
    author = models.ForeignKey(Gallery, on_delete=models.DO_NOTHING, related_name='author_images', verbose_name='Автор')
    title = models.CharField(max_length=300, verbose_name='Название картины')
    banner = models.ImageField(upload_to='gallery-images', blank=True, null=True,
                               verbose_name='Квадратное изображение картины')
    image = models.ImageField(upload_to='gallery-images', verbose_name='Картина')

    def __str__(self):
        return f'{self.author} - {self.title}'

    class Meta:
        verbose_name_plural = 'Галерея - Картины'
        verbose_name = 'Галерея - Картины'


class GalleryBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Галерея"')

    def __str__(self):
        return 'Банер "Галерея"'

    class Meta:
        verbose_name_plural = 'Галерея - банер'
        verbose_name = 'Галерея - банер'


class Contacts(models.Model):
    address = RichTextField(blank=True, null=True, verbose_name='Адрес')
    email = models.CharField(max_length=200, verbose_name='Почта')
    phone = RichTextField(blank=True, null=True, verbose_name='Телефон')

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'


class ContactsBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Контакты"')

    def __str__(self):
        return 'Банер "Контакты"'

    class Meta:
        verbose_name_plural = 'Контакты - банер'
        verbose_name = 'Контакты - банер'


class NPA(models.Model):
    text = RichTextField(blank=True, null=True, verbose_name='Содержание НПА')

    def __str__(self):
        return 'НПА'

    class Meta:
        verbose_name_plural = 'НПА'
        verbose_name = 'НПА'


class NPABanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "НПА"')

    def __str__(self):
        return 'Банер "НПА"'

    class Meta:
        verbose_name_plural = 'НПА - банер'
        verbose_name = 'НПА - банер'


class Management(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    position = models.CharField(max_length=200, blank=True, null=True, verbose_name='Должность')
    image = models.ImageField(upload_to='management-images', verbose_name='Фото')
    text = RichTextField(blank=True, null=True, verbose_name='Биография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Руководство'
        verbose_name = 'Руководство'


class Employees(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    position = models.CharField(max_length=200, blank=True, null=True, verbose_name='Должность')
    image = models.ImageField(upload_to='management-images', verbose_name='Фото')
    instagram = models.CharField(max_length=200, blank=True, null=True, verbose_name='Инстаграм')
    telegram = models.CharField(max_length=200, blank=True, null=True, verbose_name='Телеграм')
    facebook = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фейсбук')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудники'


class Logo(models.Model):
    logo = models.ImageField(upload_to='logotype', verbose_name='Логотип')

    def __str__(self):
        return 'Логотип'

    class Meta:
        verbose_name_plural = 'Логотип'
        verbose_name = 'Логотип'


class SocialMedia(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='Инстаграм')
    telegram = models.CharField(max_length=200, verbose_name='Телеграм')
    facebook = models.CharField(max_length=200, verbose_name='Фейсбук')
    twitter = models.CharField(max_length=200, verbose_name='Твиттер')
    vk = models.CharField(max_length=200, verbose_name='ВКонтакте')

    def __str__(self):
        return 'Социальные сети'

    class Meta:
        verbose_name_plural = 'Соц. сети'
        verbose_name = 'Соц. сети'


class SiteGuide(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    link = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ссылка')
    link_oder = models.CharField(max_length=200, default='0', blank=True, null=True, verbose_name='Ссылка URL')
    image = models.ImageField(upload_to='management-images', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наводка по сайту'
        verbose_name = 'Наводка по сайту'


class Manas(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название Про Манас')
    tag = models.CharField(max_length=200, blank=True, null=True, verbose_name='Тег Про Манас')
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Про Манас'
        verbose_name = 'Про Манас'


class ManasFile(models.Model):
    manas = models.ForeignKey(Manas, on_delete=models.CASCADE, related_name='manas_files')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название кнопки')
    file = models.FileField(upload_to='manas-files', blank=True, null=True, verbose_name='Файл прикрепить')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка на видео')


class ManasBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Манас"')

    def __str__(self):
        return 'Банер "Манас"'

    class Meta:
        verbose_name_plural = 'Манас - банер'
        verbose_name = 'Манас - банер'


class Archive(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название архива')
    tag = models.CharField(max_length=200, blank=True, null=True, verbose_name='Тег архива')
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')
    text = RichTextField(blank=True, null=True, verbose_name='Содержание архива')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Архив'
        verbose_name = 'Архив'


class ArchiveBanner(models.Model):
    image = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='Банер раздела "Архив"')

    def __str__(self):
        return 'Банер "Архив"'

    class Meta:
        verbose_name_plural = 'Архив - банер'
        verbose_name = 'Архив - банер'


class Mail(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.date.date()}) {self.name}  -  {self.email}'

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Письма'
        verbose_name = 'Письма'

