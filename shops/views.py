from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from shops.filters import CountryFilter
from shops.models import FactoryStore, Retailer, Entrepreneur, Products
from shops.permissions import CustomPermissions, DestroyPermission
from shops.serializers import ProductUpdateSerializer, FactoryStoreListSerializer, ProductCreateSerializer, \
    ProductsListSerializer, ProductDestroySerializer, FactoryStoreCreateSerializer, FactoryStoreUpdateSerializer, \
    FactoryStoreDestroySerializer, RetailerListSerializer, RetailerCreateSerializer, RetailerUpdateSerializer, \
    RetailerDestroySerializer, EntrepreneurCreateSerializer, EntrepreneurUpdateSerializer, EntrepreneurListSerializer, \
    ProductDetailSerializer, FactoryStoreDetailSerializer, RetailerDetailSerializer, EntrepreneurDetailSerializer, \
    EntrepreneurDestroySerializer


class ProductsCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = ProductCreateSerializer


class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = ProductsListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]


class ProductRetrieveView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class ProductUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class ProductDestroyView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductDestroySerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class FactoryStoreListView(ListAPIView):
    queryset = FactoryStore.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = FactoryStoreListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title"]
    ordering = ["title"]


class FactoryStoreRetrieveView(RetrieveAPIView):
    queryset = FactoryStore.objects.all()
    serializer_class = FactoryStoreDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class FactoryStoreCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = FactoryStoreCreateSerializer


class FactoryStoreUpdateView(UpdateAPIView):
    queryset = FactoryStore.objects.all()
    serializer_class = FactoryStoreUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class FactoryStoreDestroyView(DestroyAPIView):
    queryset = FactoryStore.objects.all()
    serializer_class = FactoryStoreDestroySerializer
    permission_classes = [DestroyPermission]


class RetailerListView(ListAPIView):
    queryset = Retailer.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = RetailerListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class RetailerRetrieveView(RetrieveAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class RetailerCreateView(CreateAPIView):
    model = Retailer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = RetailerCreateSerializer


class RetailerUpdateView(UpdateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class RetailerDestroyView(DestroyAPIView):
    queryset = Retailer.objects.all()
    permission_classes = [DestroyPermission]
    serializer_class = RetailerDestroySerializer


class EntrepeneurListView(ListAPIView):
    queryset = Entrepreneur.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = EntrepreneurListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class EntrepreneurRetrieveView(RetrieveAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class EntrepreneurCreateView(CreateAPIView):
    model = Entrepreneur
    permission_classes = [CustomPermissions]
    serializer_class = EntrepreneurCreateSerializer


class EntrepreneurUpdateView(UpdateAPIView):
    queryset = Entrepreneur.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = EntrepreneurUpdateSerializer


class EntrepreneurDestroyView(DestroyAPIView):
    queryset = Entrepreneur.objects.all()
    permission_classes = [DestroyPermission]
    serializer_class = EntrepreneurDestroySerializer
