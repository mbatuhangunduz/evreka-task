from django.db import models


class Bin(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return f'{self.latitude}  {self.longitude}'


class Operation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class BinOperation(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="bin_operations")
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name="operation_bins")
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()

    def __str__(self):
        return str(self.collection_frequency)