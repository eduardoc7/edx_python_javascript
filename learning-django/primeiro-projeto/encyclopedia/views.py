from django.shortcuts import render

import markdown2
from django import forms

from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util


class CreatePage(forms.Form):
    title = forms.CharField(label="Page Title")
    content = forms.CharField(label="Page Content", widget=forms.Textarea(
        attrs={
            "placeholder": "Type here the content of this especially wiki. The content should be write in Markdown.",
            "style": "width: 600px; height: auto; min-height: 500px;"
        }
    ))


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
        searched = [entry for entry in util.list_entries() if title[0] == entry[0].lower()]
        return render(request, "encyclopedia/page-not-found.html", {
            "title": title,
            "entries": searched,
            "entries2": util.list_entries()
        })


def search(request):
    query = request.POST["q"].lower()
    entries = util.list_entries()

    if query in [entry.lower() for entry in entries]:
        return HttpResponseRedirect(f'wiki/{query}')
    else:
        return show_page(request, query)


def create(request):
    if request.method == 'POST':
        form = CreatePage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html")

            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(f"wiki/{title}")
        else:
            return render(request, "encyclopedia/create-page.html", {"form": form})
    else:
        return render(request, "encyclopedia/create-page.html", {"form": CreatePage()})
