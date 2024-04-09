
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste', views.index),
    path("produtos/busca", views.pesquisa),
    path('produtos/categoria/<id>', views.listView),

]
