from django.shortcuts import render

#Importamos las vistas genericas
from django.views.generic import TemplateView, ListView
# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = "TEMPLATE_NAME"
    queryset =


