from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=50)
    item_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('PENDING', 'PENDING'), ('SHIPPED', 'SHIPPED'), ('CANCELLED', 'CANCELLED')])

    @property
    def overall_status(self):
        order_lines = Order.objects.filter(order_number=self.order_number)
        statuses = [line.status.upper() for line in order_lines]
        if 'PENDING' in statuses:
            return 'PENDING'
        # MISMATCH BETWEEN DESCRIPTION AND EXAMPLE RESULTS
        # THIS WORKS AS THE DESCRIPTION SAYS, SHIPPED ONLY IF ALL ORDERS
        # HAVE SHIPPED STATUS
        #elif 'SHIPPED' in statuses and 'CANCELLED' not in statuses:
        #    return 'SHIPPED'
        #else:
        #    return 'CANCELLED'
        # THIS OTHER WORKS AS THE EXAMPLE RESULTS
        elif 'SHIPPED' in statuses:
            return 'SHIPPED'
        else:
            return 'CANCELLED'
