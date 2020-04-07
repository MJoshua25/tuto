from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'affiche_image',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
