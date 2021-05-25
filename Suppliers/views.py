from collections import UserList, UserString
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy


from .models import Tbbeneficiarios


class IndexListView(ListView):
    template_name = 'index.html'
    model = Tbbeneficiarios
    paginate_by = 15
    ordering = 'id'
    queryset = Tbbeneficiarios.objects.all()
    context_object_name = 'supliers' 


class CreateBeneficiarioView(CreateView):    
    model = Tbbeneficiarios
    template_name = 'fBeneficiarios.html'
    fields = ['nome']
    success_url = reverse_lazy('index')  

    """
    Esta lógica está dentro do CreateView, é herança do BaseCreateView, Trouxe para o código e fiz as alterações
    Acrescentando o tratamento do request.user
    """
    def get(self, request, *args, **kwargs):
        if str(request.user) == 'AnonymousUser':
            print(f'Usuário: {request.user} Desconhecido')
            return redirect('index')
        else:
            self.object = None
            print(f'Usuário:{request.user} login com sucesso!')
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
