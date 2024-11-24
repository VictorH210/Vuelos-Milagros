from django.db import models




class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class Vuelo(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Vuelo {self.id}: {self.origen} - {self.destino} ({self.fecha} a las {self.hora})"

class Pasaje(models.Model):
    pasajero = models.ForeignKey('Pasajero', on_delete=models.CASCADE)
    vuelo = models.ForeignKey('Vuelo', on_delete=models.CASCADE)
    clase = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pasaje {self.id} - {self.pasajero.nombre} {self.pasajero.apellido}"







