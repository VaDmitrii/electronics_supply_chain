from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shops.models import Products, FactoryStore, Retailer, Entrepreneur


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    product_model = serializers.CharField(required=False)

    class Meta:
        model = Products
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    product_model = serializers.CharField()

    class Meta:
        model = Products
        fields = "__all__"


class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id"]


class FactoryStoreListSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True)

    class Meta:
        model = FactoryStore
        fields = "__all__"


class FactoryStoreDetailSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True)

    class Meta:
        model = FactoryStore
        fields = "__all__"


class FactoryStoreCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)

    class Meta:
        model = FactoryStore
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "created",
        ]


class FactoryStoreUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)

    class Meta:
        model = FactoryStore
        fields = "__all__"


class FactoryStoreDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryStore
        fields = ["id"]


class RetailerListSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True)
    supplier = FactoryStoreDetailSerializer(allow_null=True)

    class Meta:
        model = Retailer
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class RetailerDetailSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True, read_only=True)
    supplier = FactoryStoreDetailSerializer(allow_null=True)

    class Meta:
        model = Retailer
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class RetailerCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field='title'
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=FactoryStore.objects.all(),
        required=False,
        allow_null=True
    )
    credit = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Retailer
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]

    def create(self, validated_data):
        supplier = FactoryStore.objects.get(id=validated_data.get("supplier").id)
        supplier_products = [product.title for product in supplier.products.all()]

        with transaction.atomic():
            retailer = Retailer.objects.create(
                title=validated_data.get("title"),
                email=validated_data.get("email"),
                city=validated_data.get("city"),
                supplier=supplier,
                credit=validated_data.get("credit")
            )

            for product in validated_data.get("products"):
                if product.title in supplier_products:
                    product_obj = Products.objects.get(title=product)
                    retailer.products.add(product_obj)
                    retailer.save()
                else:
                    raise ValidationError(
                        f"У поставщика нет продукта {product.title}"
                    )

        return retailer


class RetailerUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    supplier = serializers.PrimaryKeyRelatedField(
        required=False,
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = Retailer
        read_only_fields = ["credit"]
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class RetailerDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ["id"]


class EntrepreneurListSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field='title'
    )
    supplier = serializers.CharField(allow_null=True)

    class Meta:
        model = Entrepreneur
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class EntrepreneurDetailSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    supplier = serializers.CharField(
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Entrepreneur
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class EntrepreneurCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    supplier = serializers.CharField(required=False)
    credit = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Entrepreneur
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]

    def create(self, validated_data):
        supplier = validated_data.pop("supplier")

        with transaction.atomic():
            entrepreneur = Entrepreneur.objects.create(
                title=validated_data.get("title"),
                email=validated_data.get("email"),
                city=validated_data.get("city"),
                credit=validated_data.get("credit")
            )

            try:
                supplier_object = FactoryStore.objects.filter(title=supplier).first() \
                                  or Retailer.objects.get(title=supplier)
                entrepreneur.supplier = supplier_object
                entrepreneur.save()
            except FactoryStore.DoesNotExist and Retailer.DoesNotExist:
                raise ValidationError(f"Поставщик {supplier} не найден")

            supplier_products = [product.title for product in supplier_object.products.all()]

            for product in validated_data.get("products"):
                if product.title in supplier_products:
                    product_obj = Products.objects.get(title=product)
                    entrepreneur.products.add(product_obj)
                    entrepreneur.save()
                else:
                    raise ValidationError(
                        f"У поставщика нет продукта {product.title}"
                    )

        return entrepreneur


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    supplier = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = Entrepreneur
        read_only_fields = ["credit"]
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class EntrepreneurDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = ["id"]
