from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
import requests


def historial(request):
    if  request.user.is_authenticated:
        redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, "core/historial.html", {"compras":compras})

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in  carro:
      detalle = DetallesVenta()
      detalle.producto = producto.objects.get(codigo = item[0])
      detalle.precio = item[3]
      detalle.cantidad = item[4]
      detalle.venta = venta
      detalle.save()
      request.session["carro"] = []

      Producto = producto.objects.get(codigo = item[0])
      Producto.stock -= item[4]
      Producto.save()

    return redirect(to="carro")

def addtocar(request, codigo):
    Producto = producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
       carro.append([codigo, Producto.detalle , Producto.imagen.url , Producto.precio, 1, Producto.precio])
    
    request.session["carro"] = carro
    return redirect(to="home")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")

def DeleteItem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carro")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")

def home(request):
    contenido = producto.objects.all()
    return render(request, 'core/index.html',{'contenido': contenido, "carro" :request.session.get("carro", []) })

def logout(request):
    return logout_then_login(request, login_url='home')

def suscripcion(request):
    return render(request, 'core/suscripcion.html')

def carro(request):
    return render(request, 'core/carro.html', {"carro":request.session.get("carro",[])})

def usuario(request):
    return render(request,  'core/usuarios.html')

def perfile(request):
    return render(request, 'core/perfile.html')


def login(request):
    return render(request, 'core/login.html')

def  admin_index(request):
    contenido = producto.objects.all()
    return render(request, 'core/adminindex.html',{'contenido': contenido})

def  agregar_productos(request):
    return render(request, 'core/new_productos.html')

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
    
        registro = Registro()
    return render(request, 'core/registro.html',{'form' :registro})

def home(request):
    contenido = producto.objects.all()
    context = {'contenido' : contenido }
    if request.session.get("modificado", None):
        context["modificado"] = True
        del request.session["modificado"]
    suscrito(request, context)
    print(context)
    return render(request, 'core/index.html', context) 



def suscribir(request): 
    context = {}
    suscrito(request,  context)
    if request.method == "POST":
      if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request,  context)
      return render(request, 'core/suscripcion.html', context)
        
    else:
       
        return render(request, 'core/suscripcion.html', context)

      
   


def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]








