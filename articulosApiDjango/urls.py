
from django.contrib import admin
from django.urls import path, include

from users.api.router import router_user

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", include("articulos.urls"))
    path("api/", include('users.api.router')),
    path("api/", include(router_user.urls)),
]
