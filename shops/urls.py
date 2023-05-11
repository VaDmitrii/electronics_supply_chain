from django.urls import path

from shops import views

urlpatterns = [
    path("product/create/", views.ProductsCreateView.as_view(), name='product-create'),
    path("product/list/", views.ProductsListView.as_view(), name='products-list'),
    path("product/<int:pk>/update/", views.ProductUpdateView.as_view(), name='product-update'),
    path("product/<int:pk>/", views.ProductRetrieveView.as_view(), name='product'),
    path("product/<int:pk>/delete/", views.ProductDestroyView.as_view(), name='product-delete'),
    path("factory/create/", views.FactoryStoreCreateView.as_view(), name='factory-create'),
    path("factory/<int:pk>/update/", views.FactoryStoreUpdateView.as_view(), name='factory-update'),
    path("factory/list/", views.FactoryStoreListView.as_view(), name='factory-list'),
    path("factory/<int:pk>/", views.FactoryStoreRetrieveView.as_view(), name='factory'),
    path("factory/<int:pk>/delete/", views.FactoryStoreDestroyView.as_view(), name='factory-delete'),
    path("retailer/create/", views.RetailerCreateView.as_view(), name='retailer-create'),
    path("retailer/<int:pk>/update/", views.RetailerUpdateView.as_view(), name='retailer-update'),
    path("retailer/list/", views.RetailerListView.as_view(), name='retailer-list'),
    path("retailer/<int:pk>/", views.RetailerRetrieveView.as_view(), name='retailer'),
    path("retailer/<int:pk>/delete/", views.RetailerDestroyView.as_view(), name='retailer-delete'),
    path("entrepreneur/create/", views.EntrepreneurCreateView.as_view(), name='entrepreneur-create'),
    path("entrepreneur/<int:pk>/update/", views.EntrepreneurUpdateView.as_view(), name='entrepreneur-update'),
    path("entrepreneur/list/", views.EntrepeneurListView.as_view(), name='entrepreneur-list'),
    path("entrepreneur/<int:pk>/", views.EntrepreneurRetrieveView.as_view(), name='entrepreneur'),
    path("entrepreneur/<int:pk>/delete/", views.EntrepreneurDestroyView.as_view(), name='entrepreneur-delete'),
]
