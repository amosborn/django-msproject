from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    auction_done = models.BooleanField()
    auction_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
