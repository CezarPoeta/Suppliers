from django.forms import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from collections import UserList, UserString
from django.http import request
from django.views.generic.base import ContextMixin
from django.shortcuts import redirect


from .models import Tbbeneficiarios
from .forms import BeneficiariosModelForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return super().get_context_data(**kwargs)


class IndexListView(ListView):
    model = Tbbeneficiarios
    template_name = 'flstbeneficiarios.html'
    paginate_by = 15
    ordering = 'id'
    queryset = Tbbeneficiarios.objects.all()
    context_object_name = 'supliers' 


class CreateBeneficiarioView(CreateView):    
    model = Tbbeneficiarios
    template_name = 'fBeneficiarios.html'
    fields = ['useradm','nome']
    success_url = reverse_lazy('index')

    """
    Esta lógica está dentro do CreateView, é herança do BaseCreateView, Trouxe para o código e fiz as alterações
    Acrescentando o tratamento do request.user
    """
    def get(self, request, *args, **kwargs):       
        if str(request.user) == 'AnonymousUser':
            return redirect('index')
        else:
            self.object = None
            return super().get(request, *args, **kwargs)

    
class UpdateBeneficiarioView(UpdateView):
    model = Tbbeneficiarios
    template_name = 'fBeneficiarios.html'
    fields = ['nome']
    success_url = reverse_lazy('index')  


class DeleteBeneficiarioView(DeleteView):
    model = Tbbeneficiarios
    template_name = 'fdel-Beneficiarios.html'
    success_url = reverse_lazy('index')  
