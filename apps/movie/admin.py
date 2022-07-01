from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from .models import Movie, MovieImage


class InLineMovieImage(admin.TabularInline):
    model = MovieImage
    extra = 1
    fields = ('image', )


class MovieAdmin(admin.ModelAdmin):
    inlines = [InLineMovieImage,]
    list_display = ('title', 'image')
    list_filter = ('genre',)

    def image(self, obj):
        img = obj.images.first()
        if img:
            return mark_safe(f"<img src='{img.image.url}' width ='80', height='80', style='object-fit: contain' />")


admin.site.register(Movie, MovieAdmin)

