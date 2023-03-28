

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


admin.site.register(ResearchBanner)
admin.site.register(ProjectBanner)
admin.site.register(Partner)
admin.site.register(AboutBanner)
admin.site.register(NewsBanner)
admin.site.register(GalleryBanner)
admin.site.register(ArchiveBanner)
admin.site.register(ContactsBanner)
admin.site.register(NPABanner)
admin.site.register(ManasBanner)
admin.site.register(Mail)


@admin.register(SocialMedia)
class SocialMediaImagesAdminList(TranslationAdmin):
    pass


@admin.register(GalleryImages)
class GalleryImagesAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(Employees)
class EmployeesAdminList(TranslationAdmin):
    list_display = ('id', 'name', )


@admin.register(Management)
class ManagementAdminList(TranslationAdmin):
    list_display = ('id', 'name', )


@admin.register(SiteGuide)
class SiteGuideAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(ResearchCategory)
class ResearchCategoryAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(OnlineMagazine)
class OnlineMagazineAdminList(TranslationAdmin):
    list_display = ('id', 'button', )


@admin.register(Statistic)
class StatisticAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(Logo)
class LogoAdminList(TranslationAdmin):
    pass


@admin.register(AboutPage)
class AboutAdminList(TranslationAdmin):
    pass


@admin.register(HomeAbout)
class HomeAboutAdminList(TranslationAdmin):
    pass


@admin.register(Research)
class ResearchAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(Project)
class ProjectAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(News)
class NewsAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(NPA)
class NPAAdminList(TranslationAdmin):
    pass


@admin.register(Gallery)
class GalleryAdminList(TranslationAdmin):
    list_display = ('id', 'title', )


@admin.register(Archive)
class ArchiveAdminList(TranslationAdmin):
    list_display = ('tag', 'title')


@admin.register(Contacts)
class ContactsAdminList(TranslationAdmin):
    pass


class ManasFileAdmin(admin.TabularInline):
    model = ManasFile
    fields = ('title', 'file', 'link')
    max_num = 100
    extra = 1


@admin.register(Manas)
class ManasAdminList(TranslationAdmin):
    list_display = ('title',)
    inlines = [ManasFileAdmin]


