from django.contrib import admin
from .models import Movie, ComingMovie


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'grade', 'poster_url', 'book_url')
    search_fields = ("name",)


class ComingMovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'grade', 'poster_url', 'book_url')
    search_fields = ("name",)


admin.site.register(Movie, MovieAdmin)
admin.site.register(ComingMovie, ComingMovieAdmin)
