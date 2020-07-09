from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show_page(request, title):
    for entry in util.list_entries():
        if entry == title:
            pagemd = util.get_entry(title)
            content = markdown2.markdown(pagemd)
            return render(request, "encyclopedia/show-requested.html", {
                "content": content
            })

    return render(request, "encyclopedia/page-not-found.html", {
        "title": title,
        "entries": util.list_entries()
    })
