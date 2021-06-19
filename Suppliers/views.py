#from django.forms import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

#from collections import UserList, UserString
#from django.http import request
#from django.views.generic.base import ContextMixin


from .models import Tbbeneficiarios
from .forms import BeneficiariosModelForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return super().get_context_data(**kwargs)


class IndexListView(ListView):
    model = Tbbeneficiarios
    template_name = 'lst_Beneficiarios.html'
    programa = 'Beneficiarios'
    paginate_by = 15
    ordering = '-id'
    queryset = Tbbeneficiarios.objects.all()
    context_object_name = 'supliers' 


class CreateBeneficiarioView(CreateView):    
    model = Tbbeneficiarios
    template_name = 'frm_Beneficiarios.html'
    fields = ['nome',]
    success_url = reverse_lazy('lst_beneficiarios')
    """
    Esta lógica está dentro do CreateView, é herança do BaseCreateView, Trouxe para o código e fiz as alterações
    Acrescentando o tratamento do request.user
    """
    def get(self, request, *args, **kwargs):       
        if str(request.user) == 'AnonymousUser':
            return redirect('lst_beneficiarios')
        else:
            self.object = None
            return super().get(request, *args, **kwargs)
    """
    Esta lógica me deu acesso aos dados do formulário para eu acrescentar e/ou alterar os dados informados pelo usuário
    """
    def form_valid(self, form):
#        print(f'Nome: {form.instance.nome}') # Mostra o dado informado pelo usuário no formulário
        form.instance.useradm = self.request.user
        return super().form_valid(form)


class UpdateBeneficiarioView(UpdateView):
    model = Tbbeneficiarios
    template_name = 'frm_Beneficiarios.html'
    fields = ['nome',]
    success_url = reverse_lazy('lst_beneficiarios')  


class DeleteBeneficiarioView(DeleteView):
    model = Tbbeneficiarios
    template_name = 'del_Beneficiarios.html'
    success_url = reverse_lazy('lst_beneficiarios')  
