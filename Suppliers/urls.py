from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView, IndexListView, CreateBeneficiarioView, UpdateBeneficiarioView, DeleteBeneficiarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('lst/', IndexListView.as_view(), name='lst_beneficiarios'),
    path('add/', CreateBeneficiarioView.as_view(), name='add_beneficiario'),
    path('<int:pk>/upd/', UpdateBeneficiarioView.as_view(), name='upd_beneficiario'),
    path('<int:pk>/del/', DeleteBeneficiarioView.as_view(), name='del_beneficiario'),
]