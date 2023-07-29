from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import BannerCard, NavbarLink
from .serializers import BannerCardSerializer, NavbarLinkSerializer


class BannerCardViewSet(ModelViewSet):
    queryset = BannerCard.objects.all()
    serializer_class = BannerCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class NavbarLinkViewSet(ModelViewSet):
    queryset = NavbarLink.objects.all()
    serializer_class = NavbarLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


