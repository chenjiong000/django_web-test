from django.contrib import admin
from .models import Movie,Myrating,Commodity,Group

admin.site.register(Group)
admin.site.register(Commodity)

admin.site.register(Movie)
admin.site.register(Myrating)

# Register your models here.
