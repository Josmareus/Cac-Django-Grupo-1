from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Escribano, ActoJuridico, Escritura
from .forms import EscribanoForm, ActoJuridicoForm



class IndexView(TemplateView):
    template_name = "index.html"


# ---- Escribanos ----
class CrearEscribanoView(CreateView):
    model = Escribano
    form_class = EscribanoForm
    # template_name = 'escribania/templates/escribania/escribano_form.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.info(self.request, "Escribano cargado exitosamente.")
        return super().form_valid(form)

class ListarEscribanosView(ListView):
    model = Escribano
    # template_name = 'listar_escribanos.html'
    context_object_name = 'escribanos'

class ActualizarEscribanoView(UpdateView):
    model = Escribano
    form_class = EscribanoForm
    # template_name = 'actualizar_escribano.html'
    success_url = reverse_lazy("listar_escribanos")

class EliminarEscribanoView(DeleteView):
    model = Escribano

    def get_success_url(self):
        return reverse_lazy("listar_escribanos")


# ---- Actos Jurídicos ----
class CrearActoJuridicoView(CreateView):
    model = ActoJuridico
    form_class = ActoJuridicoForm
    # template_name = 'escribania/templates/escribania/actojuridico_form.html'
    success_url = reverse_lazy("listar_actos_juridicos")

class ListarActosJuridicosView(ListView):
    model = ActoJuridico
    # template_name = 'escribania/templates/escribania/actojuridico_list.html'
    context_object_name = 'actos_juridicos'

class ActualizarActoJuridicoView(UpdateView):
    model = ActoJuridico
    form_class = ActoJuridicoForm
    # template_name = 'escribania/templates/escribania/actojuridico_form.html'
    success_url = reverse_lazy("listar_actos_juridicos")

class EliminarActoJuridicoView(DeleteView):
    model = ActoJuridico
    success_url = reverse_lazy("listar_actos_juridicos")




# ---- Escrituras ----
class CrearEscrituraView(CreateView):
    model = Escritura
    fields = '__all__'
    success_url = reverse_lazy("listar_escrituras")

class ListarEscrituraView(ListView):
    model = Escritura
    context_object_name = 'escrituras'

class ActualizarEscrituraView(UpdateView):
    model = Escritura
    fields = '__all__'
    success_url = reverse_lazy("listar_escrituras")

class EliminarEscrituraView(DeleteView):
    model = Escritura
    success_url = reverse_lazy("listar_actos_juridicos")