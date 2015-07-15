from django.conf.urls import url
from mysite import settings
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),

    url(r'^change/desc/$', views.change_table_description),
    url(r'^change/desc/column/$', views.change_table_column_description),
    url(r'^query/tables/$', views.get_all_tables),

    url(r'^query/table/(?P<id>\d+)/$', views.get_peculiar_table_info),
]