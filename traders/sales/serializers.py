from rest_framework.serializers import ModelSerializer
from .models import Trader, Tracker, CustomUser, MyUserModel

class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = '__all__'