from django.shortcuts import render



def index(request):
    context = {
        'message': '¡Hola, bienvenido a nuestra página web!'
    }
    return render(request, 'index.html', context)
