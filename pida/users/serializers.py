from rest_framework import serializers
from testers.serializers import _TesterOrderSimpleSerializer
from purchases.serializers import _PurchaseOrderSimpleSerializer
from grouppurchases.serializers import _GroupPurchaseOrderSimpleSerializer
from .models import User, SkinConcern, Allergy, PaymentInformation, DeliveryInformation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    skin_concerns = serializers.SlugRelatedField(many=True, queryset=SkinConcern.objects.all(), slug_field='key')
    allergies = serializers.SlugRelatedField(many=True, queryset=Allergy.objects.all(), slug_field='key')
    tester_orders = _TesterOrderSimpleSerializer(many=True, read_only=True)
    purchase_orders = _PurchaseOrderSimpleSerializer(many=True, read_only=True)
    group_purchase_orders = _GroupPurchaseOrderSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 'id',
            'reviews',
            'username', 'password', 'gender', 'age', 'skin_type', 'skin_concerns', \
              'allergies', 'default_payment_information', 'default_delivery_information', \
              'tester_orders', 'purchase_orders', 'group_purchase_orders',
        )
        read_only_fields = (
            'reviews', 'default_payment_information', 'default_delivery_information', \
              'tester_orders', 'purchase_orders', 'group_purchase_orders',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'username'},
        }

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.default_payment_information = PaymentInformation.objects.create(owner=instance)
        instance.default_delivery_information = DeliveryInformation.objects.create(owner=instance)
        return instance


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
            'url', 'id',
            'owner', 'issuer', 'card_number', 'expiration_date', \
              'cvc', 'password_hashed', 'valid',
        )
        read_only_fields = (
            'owner', 'valid',
        )
        extra_kwargs = {
            'owner': {'lookup_field': 'username'},
        }


class DeliveryInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryInformation
        fields = (
            'url', 'id',
            'owner', 'name', 'contact', 'postal_code', \
              'address_line_road', 'address_line_detail', 'valid',
        )
        read_only_fields = (
            'owner', 'valid',
        )
        extra_kwargs = {
            'owner': {'lookup_field': 'username'},
        }
