from django.shortcuts import render, redirect
import markdown2

from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def show_page(request, title):
    if util.get_entry(title):
        content = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/show-requested.html", {
            "content": content,
            "title": title
        })
    else:
        return render(request, "encyclopedia/page-not-found.html", {
            "title": title,
            "entries": util.list_entries()
        })


def search(request):
    query = request.POST["test"].lower()
    entries = util.list_entries()

    if query in [entry.lower() for entry in entries]:
        return HttpResponseRedirect(f'wiki/{query}')
    else:
        return show_page(request, query)


