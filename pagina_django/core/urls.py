
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name= "home"),

    path('addtocar/<codigo>', addtocar, name= "addtocar"),

    path('DeleteItem/<codigo>', DeleteItem, name= "DeleteItem"),

    path('suscripcion', suscripcion, name= "suscripcion"),

    path('limpiar', limpiar),

    path('carro', carro, name= "carro"),

    path('comprar', comprar, name= "comprar"),
    
      path('historial', historial, name="historial"),

    path('login', LoginView.as_view(template_name= 'core/login.html'), name= "login"),
     
    path('logout',logout, name = "logout"),
    
    path('admin_index', admin_index, name= "admin_index"),

    path('agregar_productos',  agregar_productos, name= " agregar_productos"),

    path('perfile',  perfile, name= " perfile"),
    

    path('registro', registro, name= "registro"),

    path('usuario', usuario, name= "usuario"),

    path('suscribir', suscribir, name= "suscribir"),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
