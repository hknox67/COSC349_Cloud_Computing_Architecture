from django.contrib import admin

from .models import Card, Card_colour, Card_subtype, Card_set, Card_supertype, Card_type

admin.site.register(Card)
admin.site.register(Card_colour)
admin.site.register(Card_subtype)
admin.site.register(Card_set)
admin.site.register(Card_supertype)
admin.site.register(Card_type)
