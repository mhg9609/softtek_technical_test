from django.urls import path
from seasons_problem.views import (order_season, set_default_orders,
                                   OrderDetail, list_orders)

urlpatterns = [
    # TECHNICAL TEST PATH
    path('seasons-problem/', order_season, name='seasons_problem'),
    # THESE PATHS ARE NOT NECESSARY FOR THE TECHNICAL TEST.
    path('seasons-problem/orders-list/', list_orders, name='orders_list'),
    path('seasons-problem/order/<str:ord_id>/', OrderDetail.as_view(), name='order_detail'),
    # THIS PATH WAS CREATED JUST TO ADD THE DEFAULT VALUES TO THE DATABASE FOR TEST
    path('seasons-problem/default-orders/', set_default_orders, name='set_default_orders'), # Just created to add data for test
]
