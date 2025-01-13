from django.db import models

class Informa(models.Model):  # Renomeado para evitar conflito
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    whatsapp = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
