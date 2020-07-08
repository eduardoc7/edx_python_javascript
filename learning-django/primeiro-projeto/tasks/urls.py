from django.urls import path
from . import views

# um identificador único para as rotas de cada app
# isso é feito para não gerar um conflito de namespace: duas rotas com o mesmo nome em diferentes aplicações
app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]
