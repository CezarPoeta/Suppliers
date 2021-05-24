from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView, CreateBeneficiarioView, UpdateBeneficiarioView, DeleteBeneficiarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateBeneficiarioView.as_view(), name='add_beneficiario'),
    path('<int:pk>/upd/', UpdateBeneficiarioView.as_view(), name='upd_beneficiario'),
    path('<int:pk>/del/', DeleteBeneficiarioView.as_view(), name='del_beneficiario')
]