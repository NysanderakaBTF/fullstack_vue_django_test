from rest_framework.serializers import ModelSerializer

from .models import BannerCard, NavbarLink


class BannerCardSerializer(ModelSerializer):
    class Meta:
        model = BannerCard
        fields = '__all__'


class NavbarLinkSerializer(ModelSerializer):
    class Meta:
        model = NavbarLink
        fields = '__all__'
