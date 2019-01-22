from rest_framework import serializers
from .models import User, SkinConcern, Allergy, PaymentInformation, DeliveryInformation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'gender', 'age', 'skin_type', 'skin_concerns', \
              'allergies', 'default_payment_information', 'default_delivery_information'
        )
        read_only_fields = (
            'default_payment_information', 'default_delivery_information'
        )


class PaymentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInformation
        fields = (
            'id',
            'owner', 'issuer', 'card_number', 'expiration_date', \
              'cvc', 'password_hashed',
        )
        read_only_fields = (
            'owner',
        )


class DeliveryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInformation
        fields = (
            'id',
            'owner', 'name', 'contact', 'postal_code', \
              'address_line_road', 'address_line_detail',
        )
        read_only_fields = (
            'owner',
        )
