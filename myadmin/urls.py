
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste', views.index),
    path("<str:alim>/", views.pesquisa),
    path("produtos/busca", views.nova),
    path("produtos/busca", views.nova),

]
