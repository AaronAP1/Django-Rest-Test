from django.shortcuts import render

# Create your views here.
def mi_pagina(request):
    return render(request, 'principal.html')