from django.urls import path
from articulos import views

urlpatterns = [
    path('articulos/', views.ArticulosAPIView.as_view()),
    path('articulo/<int:pk>', views.ArticuloAPIView.as_view()),
]