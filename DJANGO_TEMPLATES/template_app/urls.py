from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative_url/', views.relative_url_templates, name='relative_url'),
]
