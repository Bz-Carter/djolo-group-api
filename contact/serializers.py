from rest_framework import serializers

class ContactSerailizer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()