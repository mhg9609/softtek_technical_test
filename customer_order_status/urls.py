from django.urls import path
from customer_order_status.views import (order_status, set_default_orders,
                                   OrderDetail, list_orders)

urlpatterns = [
    # TECHNICAL TEST PATH
    path('customer-order-status/', order_status, name='customer_order_status'),
    # THESE PATHS ARE NOT NECESSARY FOR THE TECHNICAL TEST.
    path('customer-order-status/orders-list/', list_orders, name='orders_list'),
    path('customer-order-status/order/<str:id>/', OrderDetail.as_view(), name='order_detail'),
    # THIS PATH WAS CREATED JUST TO ADD THE DEFAULT VALUES TO THE DATABASE FOR TEST
    path('customer-order-status/default-orders/', set_default_orders, name='set_default_orders'), # Just created to add data for test
]
