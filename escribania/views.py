from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Escribano, ActoJuridico, Escritura
from .forms import EscribanoForm, ActoJuridicoForm, EscrituraForm



# ---- Escribanos ----
class CrearEscribanoView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Escribano
    form_class = EscribanoForm
    success_url = reverse_lazy("index")
    permission_required = "escribania.add_escribano"

    def form_valid(self, form):
        messages.info(self.request, "Escribano cargado exitosamente.")
        return super().form_valid(form)

class ListarEscribanosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Escribano
    context_object_name = 'escribanos'
    permission_required = "escribania.view_escribano"

class ActualizarEscribanoView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Escribano
    form_class = EscribanoForm
    success_url = reverse_lazy("listar_escribanos")
    permission_required = "escribania.change_escribano"

class EliminarEscribanoView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Escribano
    permission_required = "escribania.delete_escribano"

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
    # fields = '__all__'
    form_class = EscrituraForm
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
    success_url = reverse_lazy("listar_escrituras")