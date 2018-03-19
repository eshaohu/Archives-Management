from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'archive'

urlpatterns = [
    # table list
    url(r'^TECH-archives/$', view=views.TechArchivesListView.as_view(), name='TECH-archives'),
    url(r'^GA-archives/$', view=views.GAArchivesListView.as_view() , name='GA-archives'),
    url(r'^ADM-archives/$', view=views.ADMArchivesListView.as_view() , name='ADM-archives'),

    # chart
    url(r'^chart-archives/$', TemplateView.as_view(template_name='archive/chart.html'), name='chart-archives'),

    # look content online
    url(r'^content/$', view=views.content, name='content'),

    # upload archive
    url(r'^upload/$', view=views.upload, name='upload'),
    url(r'^add/$', view=views.add, name='add'),

    # update archive
    url(r'^update_techarchive/$', view=views.update_techarchive, name='update_techarchive'),
    url(r'^update_GAarchive/$', view=views.update_GAarchive, name='update_GAarchive'),
    url(r'^update_ADMarchive/$', view=views.update_ADMarchive, name='update_ADMarchive'),

    url(r'^modify/$', view=views.modify, name='modify'),

    # delete archive
    url(r'^delete/$', view=views.delete, name='delete'),

]