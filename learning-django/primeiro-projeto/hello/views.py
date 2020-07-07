from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def greet(request, name):
    # função para dar hello com base no que o usuário digitar na url
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    # o terceiro argumento do render é opcional e chamado de context:
    # isto é, toda a informação que eu gostaria de passar para o template, como todas as variáveis.

