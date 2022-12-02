from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import News
from django.contrib.auth.models import User


def news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/novosti")
    form = NewsForm()
    context = {
        'form': form
    }
    return render(request, "articles.html", context)


def news_number_2(request):
    news = News.objects.all()
    return render(request, "news.html", {'news': news})


def index(request):
    return render(request, "main.html")
