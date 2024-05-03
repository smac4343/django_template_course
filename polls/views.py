import os

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def main(request):
    template = "pages/user.html"
    return render(request, template)
