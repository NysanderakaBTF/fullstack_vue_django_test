from django.urls import path

from .views import NavbarLinkViewSet, BannerCardViewSet

urlpatterns = [
    path('links/', NavbarLinkViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('banner/', BannerCardViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('links/<int:pk>', NavbarLinkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('banner/<int:pk>', BannerCardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

]