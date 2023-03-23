from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    second_email = models.EmailField(null=True)
    name = models.CharField(max_length=64, null = True)
    invoice = models.FileField(null=True, upload_to='uploads/%Y/%m/%d')
    user_uuid = models.UUIDField(editable=False, null=True)
    discount_size=models.DecimalField(max_digits=5, decimal_places=5, null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol="IPv4")

    def __str__(self):
        return self.name
