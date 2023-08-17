from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html", context={}, status =200)


def dynamic_view(request, id, *args, **kwargs):
    return HttpResponse(f"<p>hello{id}</p>")
