from django.shortcuts  import render

from django.http import HttpResponse

task = ["comida", "bar", "baz"]
def index(request):
    retunr render (request, "task/index.html", {
        "tasks": task
    })
