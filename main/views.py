from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, r"main/templates/login.html")

def inicio(request):
    return render(request, r"main/templates/inicio.html")