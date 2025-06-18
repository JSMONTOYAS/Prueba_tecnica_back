from django.db import models

class Aspirante(models.Model):
    marca = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    aspirante = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca} - {self.aspirante}"
