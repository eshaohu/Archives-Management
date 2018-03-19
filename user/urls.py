from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^$', view=TemplateView.as_view(template_name='user/login.html'), name='index'),

    url(r'^login/$', view=views.login, name='login'),
    url(r'^users/$', view=TemplateView.as_view(template_name='user/users.html'), name='users'),

    # edit user info
    url(r'^edit/$', view=views.edit, name='edit'),
    url(r'^modify/$', view=views.modify, name='modify'),


    # calendar and memo
    url(r'^calendar/$', view=views.calendar, name='calendar'),
    url(r'^MemoAdd/$', view=views.MemoAddView.as_view(), name='MemoAdd'),
    url(r'^MemoEdit/$', view=views.MemoEditView.as_view(), name='MemoEdit'),
    url(r'^MemoDel/$', view=views.MemoDelView.as_view(), name='MemoDel'),


    url(r'^logout/$', view=views.logout, name='logout'),
]