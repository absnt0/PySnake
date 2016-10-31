from django.contrib import admin
from .models import ColorScheme, HighScore

# Register your models here.


class ColorSchemeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name",  {'fields': ['name']}),
        ('Snake Color', {'fields': ['snake_R', 'snake_G', 'snake_B']}),
        ('Apple Color', {'fields': ['apple_R', 'apple_G', 'apple_B']}),
        ('Walls Color', {'fields': ['walls_R', 'walls_G', 'walls_B']}),
        ('Background Color', {'fields': ['background_R', 'background_G', 'background_B']})
    ]

class HighScoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')

admin.site.register(ColorScheme, ColorSchemeAdmin)
admin.site.register(HighScore, HighScoreAdmin)