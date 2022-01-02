from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Bill, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username', 'id')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)

        return user

class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', 'id']

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ['id', 'create_user', 'isCalc', 'date', 'title', 'amount', 'pocket', 'category', 'subcategory', 'memo']
