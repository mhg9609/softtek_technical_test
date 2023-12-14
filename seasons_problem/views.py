from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime
from seasons_problem.models import Order

# TECHNICAL TEST FUNCTION
@api_view(['GET'])
def order_season(request):
    orders = Order.objects.all()
    order_list = [{'ord_id': order.ord_id, 'season': order.season} for order in orders]
    return Response(order_list, status=200)

# THIS FUNCTION IS NOT NECESSARY FOR THE TECHNICAL TEST.
@api_view(['GET'])
def list_orders(request):
    orders = Order.objects.all()
    order_list = [{
        'ord_id': order.ord_id,
        'ord_dt': order.ord_dt,
        'qt_ordd': order.qt_ordd,
        'season': order.season
    } for order in orders]
    return Response(order_list, status=200)

# THIS FUNCTION WAS CREATED JUST TO ADD THE DEFAULT VALUES TO THE DATABASE FOR TEST.
@api_view(['GET'])
def set_default_orders(request):
    Order.objects.all().delete()
    orders = [
        ('113-8909896-6940269', '2019-09-23', 1),
        ('114-0291773-7262677', '2020-01-01', 1),
        ('114-0291773-7262697', '2019-12-05', 1),
        ('114-9900513-7761000', '2020-09-24', 1),
        ('112-5230502-8173028', '2020-01-30', 1),
        ('112-7714081-3300254', '2020-05-02', 1),
        ('114-5384551-1465853', '2020-04-02', 1),
        ('114-7232801-4607440', '2020-10-09', 1),
    ]

    for ord_id, ord_dt, qt_ordd in orders:
        order = Order(
            ord_id=ord_id,
            ord_dt=datetime.strptime(ord_dt, '%Y-%m-%d'),
            qt_ordd=qt_ordd
        )
        order.save()
    return Response({'message': 'Default orders added.'}, status=200)

# THIS CLASS IS NOT NECESSARY FOR THE TECHNICAL TEST.
class OrderDetail(APIView):
    def get(self, request, ord_id):
        try:
            order = Order.objects.get(ord_id=ord_id)
            return Response({
                'ord_id': order.ord_id,
                'season': order.season,
                'ord_dt': order.ord_dt,
                'qt_ordd': order.qt_ordd
            }, status=200)
        except Order.DoesNotExist:
            return Response({'message': 'Order does not exist.'}, status=404)

    def delete(self, request, ord_id):
        try:
            order = Order.objects.get(ord_id=ord_id)
            order.delete()
            return JsonResponse({'message': 'Order deleted.'}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order does not exist.'}, status=404)

    def put(self, request, ord_id):
        try:
            order = Order.objects.get(ord_id=ord_id)
            order.ord_id = request.data.get('ord_id', order.ord_id)
            order.ord_dt = datetime.strptime(request.data.get('ord_dt', order.ord_dt.strftime('%Y-%m-%d')), '%Y-%m-%d')
            order.qt_ordd = request.data.get('qt_ordd', order.qt_ordd)
            order.save()
            return JsonResponse({'message': 'Order updated.'}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order does not exist.'}, status=404)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def post(self, request, ord_id):
        try:
            ord_id = request.data.get('ord_id')
            ord_dt = datetime.strptime(request.data.get('ord_dt'), '%Y-%m-%d')
            qt_ordd = request.data.get('qt_ordd')
            order = Order(
                ord_id=ord_id,
                ord_dt=ord_dt,
                qt_ordd=qt_ordd
            )
            order.save()
            return Response({'message': 'Order created.'}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)
