from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Escribano, ActoJuridico, Escritura
from .forms import EscribanoForm, ActoJuridicoForm



# class IndexView(TemplateView):
#     template_name = "index.html"


# ---- Escribanos ----
class CrearEscribanoView(LoginRequiredMixin, CreateView):
    model = Escribano
    form_class = EscribanoForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.info(self.request, "Escribano cargado exitosamente.")
        return super().form_valid(form)

class ListarEscribanosView(LoginRequiredMixin, ListView):
    model = Escribano
    context_object_name = 'escribanos'

class ActualizarEscribanoView(LoginRequiredMixin, UpdateView):
    model = Escribano
    form_class = EscribanoForm
    success_url = reverse_lazy("listar_escribanos")

class EliminarEscribanoView(LoginRequiredMixin, DeleteView):
    model = Escribano

    def get_success_url(self):
        return reverse_lazy("listar_escribanos")


# ---- Actos Jurídicos ----
class CrearActoJuridicoView(LoginRequiredMixin, CreateView):
    model = ActoJuridico
    form_class = ActoJuridicoForm
    success_url = reverse_lazy("listar_actos_juridicos")

class ListarActosJuridicosView(LoginRequiredMixin, ListView):
    model = ActoJuridico
    context_object_name = 'actos_juridicos'

class ActualizarActoJuridicoView(LoginRequiredMixin, UpdateView):
    model = ActoJuridico
    form_class = ActoJuridicoForm
    success_url = reverse_lazy("listar_actos_juridicos")

class EliminarActoJuridicoView(LoginRequiredMixin, DeleteView):
    model = ActoJuridico
    success_url = reverse_lazy("listar_actos_juridicos")




# ---- Escrituras ----
class CrearEscrituraView(LoginRequiredMixin, CreateView):
    model = Escritura
    fields = '__all__'
    success_url = reverse_lazy("listar_escrituras")

class ListarEscrituraView(LoginRequiredMixin, ListView):
    model = Escritura
    context_object_name = 'escrituras'

class ActualizarEscrituraView(LoginRequiredMixin, UpdateView):
    model = Escritura
    fields = '__all__'
    success_url = reverse_lazy("listar_escrituras")

class EliminarEscrituraView(LoginRequiredMixin, DeleteView):
    model = Escritura
    success_url = reverse_lazy("listar_actos_juridicos")