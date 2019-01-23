from rest_framework import serializers
from .models import User, SkinConcern, Allergy, PaymentInformation, DeliveryInformation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username', 'password', 'gender', 'age', 'skin_type', 'skin_concerns', \
              'allergies', 'default_payment_information', 'default_delivery_information'
        )
        read_only_fields = (
            'default_payment_information', 'default_delivery_information'
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def save(self, **kwargs):
        password = self.validated_data.get('password', None)
        super().save(**kwargs)
        if password is not None:
            self.instance.set_password(password)
            self.instance.save()
        return self.instance


class PaymentInformationSerializer(serializers.HyperlinkedModelSerializer):
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


class DeliveryInformationSerializer(serializers.HyperlinkedModelSerializer):
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
