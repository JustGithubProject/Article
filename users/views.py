from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = UserRegisterForm()
    context = {'form': form}
    return render(request, "register.html", context)
