from rest_framework import serializers
from .models import User, SkinConcern, Allergy


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'gender', 'age', 'skin_type', 'skin_concerns',
            'allergies',
        )


class SkinConcernSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinConcern
        fields = (
            'id',
            'name',
        )


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = (
            'id',
            'name',
        )
