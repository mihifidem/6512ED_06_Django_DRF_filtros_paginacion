from django.db import models

class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=120)
    genero = models.CharField(max_length=60, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    publicado = models.DateField()
    stock = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
