import uuid

from django.contrib.auth.models import User
from django.http import HttpResponse
from lesson_3.models import Flower, Client, Bouquet
from decimal import Decimal


def CreateFlower(request):
    rose = Flower()
    rose.count = 7
    rose.description = "Yellow Rose"
    rose.could_use_in_bouquet = True
    rose.wiki_page = "https://en.wikipedia.org/wiki/Yellow_rose"
    rose.name = "Yellow Rose"
    rose.save()
    return HttpResponse("Flower has created")

def CreateClient(request):
    with open('requirements.txt') as file:
        tmp_file = file.read()

    client = Client.objects.create(**{
        'user' : User.objects.get(pk=1),
        'second_email' : 'admin3@admin1.com',
        'name' : 'MyName3',
        'invoice' : tmp_file,
        'user_uuid' : uuid.uuid4(),
        'discount_size' : Decimal("0.000052"),
        'client_ip' : "192.0.2.3"
    })
    return HttpResponse(f"Created: {client}")

def GetFlower(request):
    price = Bouquet.shop.get(pk=1).price
    return HttpResponse(price)
