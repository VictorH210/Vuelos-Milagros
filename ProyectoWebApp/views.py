from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pasaje, Vuelo, Pasajero
from decimal import Decimal, InvalidOperation




def home(request):

    return render(request, "ProyectoWebApp/home.html")

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

def contacto(request):  
    return render(request, "ProyectoWebApp/contacto.html")

def enviar_contacto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        # Validar que los campos no estén vacíos
        if not nombre or not email or not mensaje:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('contacto')  # Redirige al formulario si algún campo está vacío

        try:
            # Aquí iría el código para procesar el mensaje, como enviarlo por correo
            # Si todo es correcto, muestra el mensaje de éxito
            messages.success(request, "¡Tu mensaje ha sido enviado correctamente! Nos pondremos en contacto contigo pronto.")
            return redirect('contacto')  # Redirige después de enviar el mensaje

        except Exception as e:
            # Si ocurre un error
            messages.error(request, f"Hubo un error al enviar tu mensaje. Por favor intenta de nuevo más tarde. Error: {e}")
            return redirect('contacto')  # Redirige al mismo formulario si hay un error

    return render(request, 'ProyectoWebApp/contacto.html')



def crear_pasajero(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        # Validar los campos
        if not nombre or not apellido or not dni or not email:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('crear_pasajero')  # Redirige al mismo formulario si hay campos vacíos

        try:
            # Crear un nuevo pasajero
            pasajero = Pasajero.objects.create(
                nombre=nombre,
                apellido=apellido,
                dni=dni,
                email=email,
                telefono=telefono
            )
            # Si el pasajero fue creado exitosamente, mostrar mensaje de éxito
            messages.success(request, "¡Pasajero creado con éxito!")
            return redirect('crear_pasajero')  # Redirige para evitar reenvío del formulario al recargar

        except Exception as e:
            # Si hay un error al crear el pasajero
            messages.error(request, f"Hubo un error al crear el pasajero. Error: {e}")
            return redirect('crear_pasajero')  # Redirige al mismo formulario si hay un error

    # Si el método no es POST, renderiza el formulario vacío
    return render(request, 'ProyectoWebApp/crear_pasajero.html')


def servicios(request):
    return render(request, 'ProyectoWebApp/servicios.html')

def crear_pasaje(request):
    if request.method == "POST":
        pasajero_id = request.POST.get('pasajero')
        vuelo_id = request.POST.get('vuelo')
        clase = request.POST.get('clase')
        precio_str = request.POST.get('precio')

        if not pasajero_id or not vuelo_id or not clase or not precio_str:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('crear_pasaje')

        try:
            precio = Decimal(precio_str)  

        except InvalidOperation:
          
            messages.error(request, "El precio debe ser un número válido.")
            return redirect('crear_pasaje')

        try:
    
            pasajero = Pasajero.objects.get(id=pasajero_id)
            vuelo = Vuelo.objects.get(id=vuelo_id)


            pasaje = Pasaje.objects.create(
                pasajero=pasajero,
                vuelo=vuelo,
                clase=clase,
                precio=precio
            )


            messages.success(request, "¡Tu pasaje ha sido creado con éxito!")
            return redirect('crear_pasaje')

        except Exception as e:
            messages.error(request, f"Hubo un error al crear el pasaje. Por favor intenta de nuevo más tarde. Error: {e}")
            return redirect('crear_pasaje')


    pasajeros = Pasajero.objects.all()
    vuelos = Vuelo.objects.all()
    return render(request, 'ProyectoWebApp/crear_pasaje.html', {'pasajeros': pasajeros, 'vuelos': vuelos})


def crear_vuelo(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        origen = request.POST.get('origen')
        destino = request.POST.get('destino')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        # Validar los campos
        if not origen or not destino or not fecha or not hora:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('crear_vuelo')  # Redirige al mismo formulario si hay campos vacíos

        try:
            # Crear un nuevo vuelo
            vuelo = Vuelo.objects.create(
                origen=origen,
                destino=destino,
                fecha=fecha,
                hora=hora
            )
            # Si el vuelo fue creado exitosamente, mostrar mensaje de éxito
            messages.success(request, "¡Tu vuelo ha sido creado con éxito!")
            return redirect('crear_vuelo')  # Redirige para evitar reenvío del formulario al recargar

        except Exception as e:
            # Si hay un error al crear el vuelo
            messages.error(request, f"Hubo un error al crear el vuelo. Por favor intenta de nuevo más tarde. Error: {e}")
            return redirect('crear_vuelo')  # Redirige al mismo formulario si hay un error

    # Si el método no es POST, renderiza el formulario vacío
    return render(request, 'ProyectoWebApp/crear_vuelo.html')





