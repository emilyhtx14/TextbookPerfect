from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100, default='')
    name = serializers.CharField(max_length=100, default='')
    rewards = serializers.DecimalField(decimal_places=2, max_digits=200, default=10000.00)
    balance = serializers.DecimalField(decimal_places=2, max_digits=200, default=10000.00)

    def create(self,validated_data):
        return Account.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('title', instance.type)
        instance.name = validated_data.get('title', instance.name)
        instance.rewards = validated_data.get('title', instance.rewards)
        instance.balance = validated_data.get('title', instance.balance)
        instance.save()
        return instance