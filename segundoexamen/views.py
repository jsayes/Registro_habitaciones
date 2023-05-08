from django.shortcuts import render
from django.http import HttpResponse
from segundoexamen.models import clientes, habitaciones, reservas

def index(request):
    return render(request, 'index.html')

def habitaciones(request):
    if request.method == 'POST':
        tipo_de_habitacion=request.POST.get('habitacion')
        print(tipo_de_habitacion)
        if tipo_de_habitacion == 'sencilla':
            return render(request, 'sencilla.html')
        elif tipo_de_habitacion == 'doble':
            return render(request, 'doble.html')
        elif tipo_de_habitacion == 'suite':
            return render(request, 'suite.html')
        else:
            return render(request, 'index.html')

def reserva(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        email = request.POST['email']
        noches = request.POST['noches']
        huespedes = request.POST['huespedes']
        precio = 50
        total = precio * int(noches)

        nombre1 = request.POST['nombre']
        celular2 = request.POST['celular']
        email2 = request.POST['email']
        noches2 = request.POST['noches']
        huespedes2 = request.POST['huespedes']
  #      total2 = precio * int(noches)

        cliente = clientes(celular=celular2, nombre=nombre1, correo=email2)
        cliente.save()

        reserva = reservas(noches=noches2, huespedes=huespedes2)
        reserva.save()

#        habitacion = habitaciones(precio=total2)
 #       habitacion.save()


    return render(request, 'reserva.html',{
        'nombre': nombre,
        'celular': celular,
        'email': email,
        'noches': noches,
        'huespedes': huespedes,
        'total':total

    })

def reserva_doble(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        email = request.POST['email']
        noches = request.POST['noches']
        huespedes = request.POST['huespedes']
        precio = 40
        total = precio * int(noches)

        nombre1 = request.POST['nombre']
        celular2 = request.POST['celular']
        email2 = request.POST['email']
        noches2 = request.POST['noches']
        huespedes2 = request.POST['huespedes']


        cliente = clientes(celular=celular2, nombre=nombre1, correo=email2)
        cliente.save()

        reserva = reservas(noches=noches2, huespedes=huespedes2)
        reserva.save()


    return render(request, 'reserva_doble.html',{
        'nombre': nombre,
        'celular': celular,
        'email': email,
        'noches': noches,
        'total':total
    })

def reserva_suite(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        email = request.POST['email']
        noches = request.POST['noches']
        huespedes = request.POST['huespedes']
        precio = 60
        total = precio * int(noches)

        nombre1 = request.POST['nombre']
        celular2 = request.POST['celular']
        email2 = request.POST['email']
        noches2 = request.POST['noches']
        huespedes2 = request.POST['huespedes']


        cliente = clientes(celular=celular2, nombre=nombre1, correo=email2)
        cliente.save()

        reserva = reservas(noches=noches2, huespedes=huespedes2)
        reserva.save()

    return render(request, 'reserva_suite.html',{
        'nombre': nombre,
        'celular': celular,
        'email': email,
        'noches': noches,
        'total':total
    })





