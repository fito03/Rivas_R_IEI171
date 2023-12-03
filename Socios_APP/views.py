from django.shortcuts import render, redirect
from .models import Socio
from .form import SocioForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listado(request):
    socios = Socio.objects.all()
    data = {
        'socios': socios
    }
    return render(request, 'listar.html', data)

def agregar(request):
    form = SocioForm()
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listado')
        
    data = {
        'titulo': 'Agregar Socio',
        'form': form
    }
    return render(request, 'agregar_editar.html', data)

def editar(request, id):
    socio = Socio.objects.get(id=id)
    form = SocioForm(instance=socio)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('/listado')
    data = {
        'titulo': 'Editar Socio',
        'form': form
    }
    return render(request, 'agregar_editar.html', data)

def eliminar(request, id):
    socio = Socio.objects.get(id=id)
    socio.delete()
    return redirect('/listado')

def usuario(request):
    return render(request, 'usuario.html')