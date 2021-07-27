from rango import views
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
]

