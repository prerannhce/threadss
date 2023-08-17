from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tweet
from django.shortcuts import render
import random
from templates.tweets.forms import TweetForm

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 122)} for x in qs]   
    data ={
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def dynamic_view(request, id, *args, **kwargs):
    return HttpResponse(f"<p>hello{id}</p>")
  