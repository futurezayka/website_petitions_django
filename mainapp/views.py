from django.shortcuts import render


def index_page(request):
    return render(request, 'mainapp/index.html')


def about_us(request):
    return render(request, 'mainapp/about.html')
