from django.shortcuts import render

def index(request):
    return render(request, 'sample/index.html')

def another(request):
    return render(request, 'sample/another.html')