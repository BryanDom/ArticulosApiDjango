from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

# esto significa que se va a registrar el viewset en la ruta users y se va a registrar en el router
router_user.register(prefix='users', basename='users', viewset=UserApiViewSet)


# esto es un API View, cosas distintas
urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # sus datos personales es lo que devuelve el endpoint auth/me/
    path('auth/me/', UserView.as_view(), name='user'),
]