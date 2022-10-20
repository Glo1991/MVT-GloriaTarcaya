from django.http import HttpResponse
#from readline import append_history_file
from django.shortcuts import render
from AppCoder.models import Familia
from datetime import *
#from dateutil.relativedelta import relativedelta
#from django.http.response import HttpResponse

def familia(request, nombre, apellido, fecha_nac):
    
    familia=Familia(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, edad =int((datetime.now() - datetime.strptime(fecha_nac, '%Y-%m-%d')).days / 365.25  ))
    familia.save()
    return HttpResponse(f"""
    <p>Nombre: {familia.nombre}</p>
    <p>Parentesco: {familia.apellido}</p>
    <p>Fecha de Nacimiento: {familia.fecha_nac}</p>
    <p>Edad: {familia.edad}</p>
    """)

def listado_familia(request):
    lista = Familia.objects.all()
    return render(request, "listado_familia.html", {"lista": lista})