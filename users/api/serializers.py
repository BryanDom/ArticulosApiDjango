from rest_framework import serializers
from users.models import User
 
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        # me va a devoler los campos que le indique en la lista
        fields = ["id", "username", "email", "first_name", "last_name","password", "is_active", "is_staff",
                  "is_superuser"]
    