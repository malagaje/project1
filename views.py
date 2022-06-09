from datetime import datetime
from django import http
from django.http import HttpResponse

def saludo(request):

    documento="""<html>
    <body>
    <h1>
    Esta es nuestra primera clase de django
    </h1>
    </body>
    </html>
    """
    return HttpResponse(documento)

def despedida(request):

    documento1="""<html>
    <body>
    <h2>
    Hasta aquí nuestra primera clase
    </h2>
    </body>
    </html>
    """
    return HttpResponse(documento1)

def damefecha(request):

    mifecha= datetime.now()

    documento2= """
    <html>
    <body>
    <h3>
    fecha y hora actuales %s
    </h3>
    </body>
    </html>
    """    % mifecha

    return HttpResponse(documento2)

def calculaEdad(request, agno):

    edadActual=18
    periodo=agno-2019
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)

