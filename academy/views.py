from django import forms
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from .models import *


def home(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    statistics = Statistic.objects.all()
    home_about = HomeAbout.objects.all()
    research_category = ResearchCategory.objects.all()
    research = Research.objects.all()
    project = Project.objects.all()
    magazine = OnlineMagazine.objects.all()
    partner = Partner.objects.all()
    guide = SiteGuide.objects.all()

    context = {'statistics': statistics, 'home_about': home_about, 'research_category': research_category,
               'research': research, 'project': project, 'magazine': magazine, 'partner': partner, 'guide': guide,
               'logo': logo, 'social': social}
    return render(request, 'home.html', context)


def about(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    abouts = AboutPage.objects.all()[0]
    banner = AboutBanner.objects.all()
    management = Management.objects.all()
    employees = Employees.objects.all()
    context = {'abouts': abouts, 'banner': banner, 'management': management, 'employees': employees,
               'logo': logo, 'social': social}
    return render(request, 'about/about.html', context)


class ManagementDetail(DetailView):
    model = Management
    template_name = 'about/management.html'
    context_object_name = 'management'
    pk_url_kwarg = 'management_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        context['banner'] = AboutBanner.objects.all()[0]
        return context


def projects(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    project = Project.objects.all()
    banner = ProjectBanner.objects.all()
    context = {'project': project, 'banner': banner, 'logo': logo, 'social': social}
    return render(request, 'projects/projects.html', context)


class ProjectsDetail(DetailView):
    model = Project
    template_name = 'projects/projects-detail.html'
    context_object_name = 'project'
    pk_url_kwarg = 'projects_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        return context


def news_page(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    news = News.objects.all()
    banner = NewsBanner.objects.all()
    context = {'news': news, 'banner': banner, 'logo': logo, 'social': social}
    return render(request, 'news/news.html', context)


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news-detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        return context


def research_page(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    research = Research.objects.all()
    banner = ResearchBanner.objects.all()
    context = {'research': research, 'banner': banner, 'logo': logo, 'social': social}
    return render(request, 'research/research.html', context)


class ResearchDetail(DetailView):
    model = Research
    template_name = 'research/research-detail.html'
    context_object_name = 'research'
    pk_url_kwarg = 'research_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        return context


def gallery_page(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    gallery = Gallery.objects.all()
    banner = GalleryBanner.objects.all()
    context = {'gallery': gallery, 'banner': banner, 'logo': logo, 'social': social}
    return render(request, 'gallery/gallery.html', context)


def contacts(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    contact = Contacts.objects.all()[0]
    banner = GalleryBanner.objects.all()
    context = {'banner': banner, 'logo': logo, 'social': social, 'contacts': contact}
    return render(request, 'contacts/contacts.html', context)


def npa(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    npa_s = NPA.objects.all()[0]
    banner = NPABanner.objects.all()
    context = {'banner': banner, 'logo': logo, 'social': social, 'npa': npa_s}
    return render(request, 'npa/npa.html', context)


class AuthorDetail(DetailView):
    model = Gallery
    template_name = 'gallery/authors.html'
    context_object_name = 'author'
    pk_url_kwarg = 'author_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        context['banner'] = GalleryBanner.objects.all()[0]
        return context


def manas(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    banner = ManasBanner.objects.all()
    manas_text = Manas.objects.all()
    context = {'banner': banner, 'logo': logo, 'social': social, 'manas_text': manas_text}
    return render(request, 'manas/manas.html', context)


class ManasDetail(DetailView):
    model = Manas
    template_name = 'manas/manas-detail.html'
    context_object_name = 'manas'
    pk_url_kwarg = 'manas_id'

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        context['banner'] = GalleryBanner.objects.all()[0]
        context['manas_files'] = ManasFile.objects.filter(manas=self.kwargs.get('manas_id'))
        return context


def archive_page(request):
    logo = Logo.objects.all()
    social = SocialMedia.objects.all()
    archive = Archive.objects.all()
    banner = NewsBanner.objects.all()
    context = {'archive': archive, 'banner': banner, 'logo': logo, 'social': social}
    return render(request, 'archive/archive.html', context)


class ArchiveDetail(DetailView):
    model = Archive
    template_name = 'archive/archive-detail.html'
    context_object_name = 'archive'
    pk_url_kwarg = 'archive_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.all()
        context['social'] = Logo.objects.all()
        return context


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'email', 'text')


class MailCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            last_sender = Mail.objects.first()
            message = f'Имя:  {last_sender.name}\n' \
                      f'Почта: {last_sender.email}\n' \
                      f'Текст обращения: {last_sender.text}'
            send_mail(
                f'Письмо от : {last_sender.name} {last_sender.email}',
                message,
                settings.EMAIL_HOST_USER,
                ['mnsait.acad@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки письма.')
