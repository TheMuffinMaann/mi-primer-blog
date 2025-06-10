from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion, ObraArte

def lista_public(request):
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/lista_public.html', {'publicaciones':publicaciones})

def lista_obras(request):
    obras = ObraArte.objects.all().order_by('fecha_creacion')
    return render(request, 'blog/lista_obras.html', {'obras': obras})
