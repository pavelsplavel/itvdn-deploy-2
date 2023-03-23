import csv
import datetime
from django.http import HttpResponse
from django.views.generic import ListView
from lesson_5.models import GameModel, GamerModel, GamerLibraryModel
from django.db.models import Q

def upload_data(request):
    with open('vgsales.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse("Done!")

class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    # queryset = GameModel.objects.filter(name__contains = "The Order: 1886")
    #____________________
    # we waht to have the exactly name of row "Hitman (2016)"
    # queryset = GameModel.objects.filter(platform = "PS4")
    # ____________________
    # list of items
    # queryset = GameModel.objects.filter(name__in=["Hitman (2016)", "Tetris"])
    # ____________________
    # greater then gt, gte, lt, lte
    # queryset = GameModel.objects.filter(na_sales__gt=1.0)
    # ____________________
    # greater then or equal
    # queryset = GameModel.objects.filter(na_sales__gte=23.2)
    # ____________________
    # name start/end with - __startswith, __endswith
    # queryset = GameModel.objects.filter(name__startswith="H")
    # ____________________
    # range
    # queryset = GameModel.objects.filter(eu_sales__range=range(1,3))
    # ____________________
    # find date by day
    # queryset = GameModel.objects.filter(year__day=1)
    # ____________________
    # find date by year
    #queryset = GameModel.objects.filter(year__year=1988)
    # ____________________
    # find null
    #queryset = GameModel.objects.filter(name__isnull=True)
    # ____________________
    # regex
    # queryset = GameModel.objects.filter(name__regex=r'^(A?|The) +')

    # ____________________ DIFFICULT QUERIES
    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="A") & Q(name__endswith="a") & Q(name__contains="ma")
    # )
    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="A") & Q(name__endswith="a")
    # )
    # ____________________
    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="A") | Q(name__endswith="B") | Q(name__endswith="C")
    # )
    # ____________________~NOT
    queryset = GameModel.objects.filter(
        ~Q(name__startswith="A") | ~Q(name__endswith="B") | ~Q(name__endswith="C")
    )

#want to find data from outer table
def relation_filter_view(request):
    data=GamerLibraryModel.objects.filter(gamer__email__contains="a")
    print(data[0].gamer.email)
    #variant 1
    # return HttpResponse(data)
    # variant 2 random sort
    return HttpResponse(data.order_by("?"))



class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains = "Hitman")

class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by('year').reverse()

class AllView(ListView):
    template_name = 'gamemodel_list.html'
    query_set = GameModel.objects.all()

class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(
        GameModel.objects.filter(name="Tetris")
    )

class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()

class ValuesView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").values("name", "platform", "year")

    def get(self, request, *args, **kwargs):
        print(GameModel.objects.filter(name="Hitman (2016)").values("name", "platform", "year"))
        print(list(GameModel.objects.all().values_list("name", "year")))
        return super().get(request, *args, **kwargs)

def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='day')
    print(data)
    return HttpResponse(data)

def get_view(request):
    data = GameModel.objects.get(id=1)
    print(data)
    return HttpResponse(data)

def create_view(request):

    # 1 Variant
    # my_self = GamerModel()
    # my_self.email = "pavelsplavel@gmail.com"
    # my_self.nickname = "Pavlo"

    # 2 Variant
    # my_self = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email = "123@gmail.com",
    #         nickname= "123"
    #     ),
    #     GamerModel(
    #         email="456@gmail.com",
    #         nickname="456"
    #     ),
    #     GamerModel(
    #         email="789@gmail.com",
    #         nickname="789"
    #     )
    # ])

    #________________
    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=10), size=10)
    # my_library.save()
    #many to many relation
    # my_library.game.set([GameModel.objects.get(pk=1),GameModel.objects.get(pk=2)])

    #____________________________
    # my_library = GamerLibraryModel.objects.create(gamer=GamerModel.objects.get(pk=10),size=10)
    # my_library.game.set([GameModel.objects.get(pk=1), GameModel.objects.get(pk=2)])

    #_______________________
    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10)
    #      ]
    # )

    # my_self.save()
    #_____________________
    my_friend = GamerModel.objects.filter(pk=10)
    my_friend.update(nickname="MySecondNickName")
    # _____________________
    # my_friend = GamerModel.objects.get(pk=10)
    # my_friend.nickname = "My Friend"
    # my_friend.save()

    # return HttpResponse(my_self)
    return HttpResponse(my_friend)

