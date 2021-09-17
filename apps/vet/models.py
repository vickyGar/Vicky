from django.db import models

# Create your models here.

class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, null=False, blank=False)
    nombre_cliente = models.CharField(max_length=20, null=False, blank=False)
    apellido_cliente = models.CharField(max_length=20, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
        ordering=['nombre_cliente']

    def _str_(self):
        return "{0}".format(self.nombre_cliente)

class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    raza=models.TextField(null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)


    class Meta:
        verbose_name='mascota'
        verbose_name_plural='mascota'
        ordering=['nombre']

    def _str_(self):
        return "{0}".format(self.nombre)


class Cita(models.Model):
    pk_cita = models.AutoField(primary_key=True, null=False, blank=False)
    fk_cliente = models.ForeignKey(cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)
    fk_mascota = models.OneToOneField(mascota, null=False, blank=False, on_delete=models.CASCADE)
