from django.contrib import admin
from lesson_5.models import GamerLibraryModel, GamerModel, GameModel

admin.site.register(GamerLibraryModel)
admin.site.register(GamerModel)
admin.site.register(GameModel)


