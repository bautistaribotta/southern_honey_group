from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    localidad = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    factura_produccion = models.BooleanField(default=False)
    cuit = models.CharField(max_length=15, null=True, blank=True)

    # Obligo a Django a llamar la tabla "clientes" en ve de "main_clientes"
    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"