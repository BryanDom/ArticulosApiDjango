from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# el decorador es para registrar el modelo en el admin de Django
# y el primer argumento es el modelo que se va a registrar
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
