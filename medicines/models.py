from django.db import models
from laboratories.models import Laboratory

class Medicine(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(default=1, null=False)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, related_name='medicines')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price_format(self):
        return f'${self.price / 100}.00'

    def __str__(self):
        return self.name
