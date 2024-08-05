

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('product_status/', views.product_status, name='product_status'),
    path('block2block/', views.block2block, name='block2block'),
    path('success/', views.success, name='success'),
    path('edit_products/', views.edit_products, name='edit_products'),
    path('edit_product_status/<str:warehouse>/<int:product_id>/', views.edit_product_status, name='edit_product_status'),
    path('transfer_product/', views.transfer_product, name='transfer_product'),
    path('transfer_products/<str:from_warehouse>/<str:to_warehouse>/', views.transfer_products, name='transfer_products'),
    path('available_slots/<str:warehouse_name>/', views.available_slots, name='available_slots'),
    path('get_products/<str:source>/<str:destination>/', views.get_products, name='get_products'),
]


