from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<str:name>", views.greet, name='greet')
    # o path possui 2 parametros que podemos passar
    # 1: o que será digitado na url após a primeira / | 2: o que será executado quando essa url for chamada
]
