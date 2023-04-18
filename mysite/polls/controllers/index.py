from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    name = request.POST
    return render(request, 'index.html', name)


def about(request):
    return render(request, 'about.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return HttpResponse("My hobbies")


def gallery(request):
    return HttpResponse("My gallery")


def interests(request):
    return render(request, 'interests.html', {})