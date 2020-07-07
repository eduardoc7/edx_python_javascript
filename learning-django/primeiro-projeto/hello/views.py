from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hello!')


def greet(request, name):
    # função para dar hello com base no que o usuário digitar na url
    return HttpResponse(f'Hello, {name}')

