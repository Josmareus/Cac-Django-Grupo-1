from django.shortcuts import render, redirect
from .models import Escribano, ActoJuridico
from .forms import EscribanoForm, ActoJuridicoForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    TemplateView,
    DeleteView,
    View,
)



def index(request):
    return render(request, "index.html")


# ----- Escribanos -----

# Vista para CREAR un Escribano
def crear_escribano(request):
    if request.method == 'POST':
        form = EscribanoForm(request.POST)
        if form.is_valid():
            messages.info(request, "Escribano cargado exitosamente.")
            return redirect(reverse("index"))
    else:
        form = EscribanoForm()
    return render(request, 'escribania/templates/escribania/escribano_form.html', {'form': form})

# LISTAR Escribanos
# def listar_escribanos(request):
#     escribanos = Escribano.objects.all()
#     return render(request, 'listar_escribanos.html', {'escribanos': escribanos})

# ACTUALIZAR un Escribano
# def actualizar_escribano(request, pk):
#     escribano = Escribano.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EscribanoForm(request.POST, instance=escribano)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_escribanos')
#     else:
#         form = EscribanoForm(instance=escribano)
#     return render(request, 'actualizar_escribano.html', {'form': form, 'escribano': escribano})



# ----- Actos Jurídicos -----

# CREAR un ActoJuridico
def crear_acto_juridico(request):
    if request.method == 'POST':
        form = ActoJuridicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_actos_juridicos')
    else:
        form = ActoJuridicoForm()
    return render(request, 'escribania/templates/escribania/actojuridico_form.html', {'form': form})

# LISTAR ActosJuridicos
def listar_actos_juridicos(request):
    actos_juridicos = ActoJuridico.objects.all()
    return render(request, 'escribania/templates/escribania/actojuridico_list.html', {'actos_juridicos': actos_juridicos})

# ACTUALIZAR un ActoJuridico
def actualizar_acto_juridico(request, pk):
    acto_juridico = ActoJuridico.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActoJuridicoForm(request.POST, instance=acto_juridico)
        if form.is_valid():
            form.save()
            return redirect('listar_actos_juridicos')
    else:
        form = ActoJuridicoForm(instance=acto_juridico)
    return render(request, 'escribania/templates/escribania/actojuridico_form.html', {'form': form, 'acto_juridico': acto_juridico})