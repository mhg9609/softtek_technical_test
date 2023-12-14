from django.db import models

class Order(models.Model):
    ord_id = models.CharField(max_length=20)
    ord_dt = models.DateField()
    qt_ordd = models.IntegerField()

    @property
    def season(self):
        if (3, 19) <= (self.ord_dt.month, self.ord_dt.day) <= (6, 19):
            return 'Spring'
        elif (6, 20) <= (self.ord_dt.month, self.ord_dt.day) <= (9, 21):
            return 'Summer'
        elif (9, 22) <= (self.ord_dt.month, self.ord_dt.day) <= (12, 20):
            return 'Fall'
        else:
            return 'Winter'

