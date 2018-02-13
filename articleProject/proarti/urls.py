from django.conf.urls import url,include
from django.contrib import admin
from.import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^article/', include('articles.urls')),
    url(r'^account/', include('accounts.urls')),
]