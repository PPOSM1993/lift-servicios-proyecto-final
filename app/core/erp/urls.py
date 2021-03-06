from core.erp.views.formapago.views import *
from core.erp.views.marca.views import *
from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.subcategory.views import *
from core.erp.views.client.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.product.views import *
from core.erp.views.sale.views import *
from core.erp.views.tests.views import TestView
from core.erp.views.proveedor.views import *
from core.erp.views.permissions.views import *

app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # subcategory
    path('subcategory/list/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/add/', SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/update/<int:pk>/', SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
    # client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # test
    path('test/', TestView.as_view(), name='test'),
    # sale
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePDFView.as_view(), name='sale_invoice_pdf'),
    # proveedor
    path('proveedor/list/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedor/add/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedor/update/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedor/delete/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
    # brand
    path('marca/list/', MarcaListView.as_view(), name='marca_list'),
    path('marca/add/', MarcaCreateView.as_view(), name='marca_create'),
    path('marca/update/<int:pk>/', MarcaUpdateView.as_view(), name='marca_update'),
    path('marca/delete/<int:pk>/', MarcaDeleteView.as_view(), name='marca_delete'),
    #forma pago
    path('formapago/list/', FormaPagoListView.as_view(), name='formapago_list'),
    path('formapago/add/', FormaPagoCreateView.as_view(), name='formapago_create'),
    path('formapago/update/<int:pk>/', FormaPagoUpdateView.as_view(), name='formapago_update'),
    path('formapago/delete/<int:pk>/', FormaPagoDeleteView.as_view(), name='formapago_delete'),
    #groups
    path('groupgroup/list/', GroupListView.as_view(), name='group_list'),
    path('group/add/', GroupCreateView.as_view(), name='group_create'),
    path('group/update/<int:pk>/',
        GroupUpdateView.as_view(), name='gorup_update'),
    path('group/delete/<int:pk>/', GroupDeleteView.as_view(), name='group_delete'),
]
