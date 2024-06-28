from django.db import models
from django.contrib.auth.models import AbstractUser

# creamos nuestro modelo de usuario personalizado
class User(AbstractUser):
    # para que no se pueda registrar un usuario con el mismo email
    email = models.EmailField(unique=True)
    # con esto le decimos a Django que el campo email es el que se va a usar para autenticar
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email