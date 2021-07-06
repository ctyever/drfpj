from rest_framework import serializers
from .models import MemberVO as member


class MemberSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = member
        fields = '__all__'

    def create(self, validated_data):
        return member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        member.objects.filter(pk=instance.username).update(**validated_data)
        return member
