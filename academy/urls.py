from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('management/<int:management_id>/', ManagementDetail.as_view(), name='management'),
    path('projects', projects, name='projects'),
    path('projects/<int:projects_id>/', ProjectsDetail.as_view(), name='projects'),
    path('news', news_page, name='news'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),
    path('archive', archive_page, name='archive'),
    path('archive/<int:archive_id>/', ArchiveDetail.as_view(), name='archive'),
    path('research', research_page, name='research'),
    path('research/<int:research_id>/', ResearchDetail.as_view(), name='research'),
    path('gallery', gallery_page, name='gallery'),
    path('gallery/<int:author_id>/', AuthorDetail.as_view(), name='gallery'),
    path('contacts', contacts, name='contacts'),
    path('contacts/mail/', MailCreateView.as_view(), name='mail'),
    path('npa', npa, name='npa'),
    path('manas', manas, name='manas'),
    path('manas/<int:manas_id>/', ManasDetail.as_view(), name='manas'),

]
