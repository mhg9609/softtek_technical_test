from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime
from customer_order_status.models import Order

# TECHNICAL TEST FUNCTION
@api_view(['GET'])
def order_status(request):
    order_numbers = set(Order.objects.values_list('order_number', flat=True))
    order_status_list = [{'order_number': order_number, 'overall_status': Order.objects.filter(order_number=order_number).first().overall_status} for order_number in order_numbers]
    return Response(order_status_list, status=200)

# THIS FUNCTION IS NOT NECESSARY FOR THE TECHNICAL TEST.
@api_view(['GET'])
def list_orders(request):
    orders = Order.objects.all()
    order_list = [{
        'id': order.id,
        'order_number': order.order_number,
        'item_name': order.item_name,
        'status': order.status,
        'overall_status': order.overall_status
    } for order in orders]
    return Response(order_list, status=200)

# THIS FUNCTION WAS CREATED JUST TO ADD THE DEFAULT VALUES TO THE DATABASE FOR TEST.
@api_view(['GET'])
def set_default_orders(request):
    Order.objects.all().delete()
    orders = [
        ('ORD_1567', 'LAPTOP', 'SHIPPED'),
        ('ORD_1567', 'MOUSE', 'SHIPPED'),
        ('ORD_1567', 'KEYBOARD', 'PENDING'),
        ('ORD_1234', 'GAME', 'SHIPPED'),
        ('ORD_1234', 'BOOK', 'CANCELLED'),
        ('ORD_1234', 'BOOK', 'CANCELLED'),
        ('ORD_9834', 'SHIRT', 'SHIPPED'),
        ('ORD_9834', 'PANTS', 'CANCELLED'),
        ('ORD_7654', 'TV', 'CANCELLED'),
        ('ORD_7654', 'DVD', 'CANCELLED')
    ]

    for order_number, item_name, status in orders:
        order = Order(
            order_number=order_number,
            item_name=item_name,
            status=status
        )
        order.save()
    return Response({'message': 'Default orders added.'}, status=200)

# THIS CLASS IS NOT NECESSARY FOR THE TECHNICAL TEST.
class OrderDetail(APIView):
    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
            return Response({
                'id': order.id,
                'order_number': order.order_number,
                'overall_status': order.overall_status,
                'item_name': order.item_name,
                'status': order.status
            }, status=200)
        except Order.DoesNotExist:
            return Response({'message': 'Order does not exist.'}, status=404)

    def delete(self, request, id):
        try:
            order = Order.objects.get(id=id)
            order.delete()
            return JsonResponse({'message': 'Order deleted.'}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order does not exist.'}, status=404)

    def put(self, request, id):
        try:
            order = Order.objects.get(id=id)
            order.order_number = request.data.get('order_number', order.order_number)
            order.item_name = request.data.get('item_name', order.item_name)
            order.status = request.data.get('status', order.status)
            order.save()
            return JsonResponse({'message': 'Order updated.'}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order does not exist.'}, status=404)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def post(self, request, id):
        try:
            order_number = request.data.get('order_number')
            item_name = request.data.get('item_name')
            status = request.data.get('status')
            order = Order(
                order_number=order_number,
                item_name=item_name,
                status=status
            )
            order.save()
            return Response({'message': 'Order created.'}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)
