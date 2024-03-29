from collections import UserList
from django.db import models
from django.contrib.auth import get_user_model
from django.http import request


class Base(models.Model):
    useradm = models.ForeignKey(get_user_model(), verbose_name="UserAdm", on_delete=models.CASCADE)
    created = models.DateField(db_column='created', auto_now_add=True)
    updated = models.DateField(db_column='updated', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Tbbeneficiarios(Base): 
    nome = models.CharField('Nome', max_length=60, blank=True, null=True) 

    def __str__(self):  
        return self.nome  
    
    class Meta: 
        # managed = False 
        db_table = 'tbbeneficiarios' 
        verbose_name = 'Beneficiário'  
        verbose_name_plural = 'Beneficiários'  

