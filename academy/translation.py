from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Manas)
class ManasTranslation(TranslationOptions):
    fields = ('tag', 'title')


@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = ('title', )


@register(HomeAbout)
class HomeAboutTranslation(TranslationOptions):
    fields = ('small_title', 'big_title', 'title', 'description')


@register(ResearchCategory)
class ResearchCategoryTranslation(TranslationOptions):
    fields = ('title', )


@register(Research)
class ResearchTranslation(TranslationOptions):
    fields = ('title', 'text')


@register(Project)
class ProjectTranslation(TranslationOptions):
    fields = ('title', 'tag', 'text')


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'tag', 'text')


@register(OnlineMagazine)
class OnlineMagazineTranslation(TranslationOptions):
    fields = ('button', )


@register(AboutPage)
class AboutPageTranslation(TranslationOptions):
    fields = ('title', 'description', 'content', 'content_desc', 'tasks', 'tasks_desc', 'mission', 'mission_desc',
              'department')


@register(Gallery)
class GalleryTranslation(TranslationOptions):
    fields = ('title', 'date', 'text')


@register(GalleryImages)
class GalleryImagesTranslation(TranslationOptions):
    fields = ('title', )


@register(Contacts)
class ContactsTranslation(TranslationOptions):
    fields = ('address', 'phone')


@register(NPA)
class NPATranslation(TranslationOptions):
    fields = ('text', )


@register(Management)
class ManagementTranslation(TranslationOptions):
    fields = ('name', 'position', 'text')


@register(Employees)
class EmployeesTranslation(TranslationOptions):
    fields = ('name', 'position', )


@register(Logo)
class LogoTranslation(TranslationOptions):
    fields = ('logo', )


@register(SocialMedia)
class SocialMediaTranslation(TranslationOptions):
    fields = ('telegram', )


@register(SiteGuide)
class SiteGuideTranslation(TranslationOptions):
    fields = ('title', )


@register(Archive)
class ArchiveTranslation(TranslationOptions):
    fields = ('title', 'tag', 'text')








