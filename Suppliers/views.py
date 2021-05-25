from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Tbbeneficiarios


class IndexListView(ListView):
    template_name = 'index.html'
    model = Tbbeneficiarios
    paginate_by = 15
    ordering = 'nome'
    queryset = Tbbeneficiarios.objects.all()
    context_object_name = 'supliers' 


class CreateBeneficiarioView(CreateView):
    model = Tbbeneficiarios
    template_name = 'fBeneficiarios.html'
    fields = ['nome']
    success_url = reverse_lazy('index')  


class UpdateBeneficiarioView(UpdateView):
    model = Tbbeneficiarios
    template_name = 'fBeneficiarios.html'
    fields = ['nome']
    success_url = reverse_lazy('index')  


class DeleteBeneficiarioView(DeleteView):
    model = Tbbeneficiarios
    template_name = 'fdel-Beneficiarios.html'
    success_url = reverse_lazy('index')  
