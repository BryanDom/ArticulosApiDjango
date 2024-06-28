from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer

# quien va poder utilizar los endpoints de este viewset es el usuario autenticado y el superusuario
class UserApiViewSet(ModelViewSet):
    # los endpoints estan protegidos por el permiso IsAdminUser
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    # aquí se define el queryset que se va a utilizar para obtener los datos
    queryset = User.objects.all()
    
    # override del método create para encriptar la contraseña
    def create(self, request, *args, **kwargs):
        # lo que va ser es que el password que se envíe en el request.data va ser encriptado
        # es decir, me agarras la contraseña, la encriptas y la guardas en la base de datos
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)
    
    # override del método update para encriptar la contraseña
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        # si el usuario quiere cambiar la contraseña, se encripta
        if password:
            # aqui hacemos la encriptación de la contraseña que se envía en el request.data
            request.data['password'] = make_password(password)
        else:
            # si no se envía una contraseña, se mantiene la contraseña que ya tiene el usuario
            request.data['password'] = request.user.password
        # se llama al método update de la clase padre para que se actualice el usuario en la base de datos
        return super().update(request, *args, **kwargs)
    

# clase para obtener los datos de un usuario autenticado
class UserView (APIView):
    # solo los usuarios autenticados y los superusuarios pueden acceder a este endpoint
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # se obtiene el usuario autenticado
        user = request.user
        # se serializa el usuario, es decir, el usuario que esta ejecutando la petición
        serializer = UserSerializer(user)
        # se retorna el usuario serializado
        return Response(serializer.data)