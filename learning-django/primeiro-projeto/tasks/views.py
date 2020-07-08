from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class NewTask(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    # armazenando as listas em cada sessão do navegador
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session['tasks']
    })


def add(request):
    # fazer uma verificação no server-side para confirmar se o form está válido
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTask()
    })
