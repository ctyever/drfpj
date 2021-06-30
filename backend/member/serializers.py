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
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('code', instance.password)
        instance.name = validated_data.get('linenos', instance.name)
        instance.email = validated_data.get('language', instance.email)
        instance.save()
        return instance
