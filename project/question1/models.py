from django.db import models

# Create your models here.


class Vehicle(models.Model):
    plate = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return str(self.plate)

    """save method is overriden to remove spaces from the plate number"""
    def save(self, *args, **kwargs):
        self.plate = self.plate.replace(" ", "")
        super(Vehicle, self).save(*args, **kwargs)
    

class NavigationRecord(models.Model):
    datetime = models.DateTimeField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="navigation_records")

    def __str__(self):
        return str(self.datetime)

