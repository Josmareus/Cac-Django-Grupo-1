from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    TemplateView,
    DeleteView,
    View,
)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Prefetch

from .forms import RegistrationForm



@login_required(login_url="/app/login")
@permission_required('users.add_user', raise_exception=True)
def sign_up(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # login(request, user)
            return redirect('/')

    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})