from rest_framework import serializers

from .models import Category, Type, Property, Space, Photo, Video, Partner


class SpaceSerializer(serializers.ModelSerializer):
    """Serializer for Space object"""
    class Meta:
        model = Space
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    """Serializer for Property object"""
    class Meta:
        model = Property
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""

    class Meta:
        model = Category
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    """Serializer for type object"""

    class Meta:
        model = Type
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    """Serializer for photo object"""

    class Meta:
        model = Photo
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    """Serializer for video object"""

    class Meta:
        model = Video
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner object"""
    class Meta:
        model = Partner
        fields = '__all__'
