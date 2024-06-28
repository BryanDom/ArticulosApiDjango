from django.db import models

class Articulo(models.Model):
    titulo  = models.CharField(max_length=100)
    contenido = models.TextField(max_length=100)
    categoria = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo