from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pregunta, Respuesta
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name= 'encuesta/index.html'
    context_object_name = 'listado_preguntas'

    def get_queryset(self):
        "Devuelve las últimas 5 preguntas"
        return Pregunta.objects.order_by('fecha')[:5]

class DetalleVista(generic.DetailView):
    model= Pregunta
    template_name = 'encuesta/detalle.html'


class ResultadoVista(generic.DetailView):
    model= Pregunta
    template_name='encuesta/resultados.html'


def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        seleccion = pregunta.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Respuesta.DoesNotExist):
        return render(request, 'encuesta/detalle.html',{
            'pregunta': pregunta,
            'error_message': 'No has seleccionado una respuesta',
        })
    else:
        seleccion.votes += 1
        seleccion.save()
        return HttpResponseRedirect(reverse('encuesta:resultados', args= (pregunta.id,)))