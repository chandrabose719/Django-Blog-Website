from django.conf.urls import url
from.import views

app_name = 'articles'

urlpatterns = [
	url(r'^$', views.all_article, name = 'all_article'),
	url(r'^create-article/$', views.create_article, name = 'create_article'),
	url(r'^auther-article/$', views.auther_article, name = 'auther_article'),
	url(r'^(?P<slug>[\w-]+)/add-comment/$', views.add_comment, name = 'add_comment'),
	url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name = 'article_detail'),
]