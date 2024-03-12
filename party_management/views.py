from django.shortcuts import render


def index(request):
    sentence = "This sentence is from index.html"
    return render(request, 'index.html', {'sentence': sentence})