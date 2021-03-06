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


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_upd'
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'contacts',
        'birth_date',
        'genre',
        'date_add',
        'date_upd',
        'status',

    )
    list_filter = (
        'status',
        'date_upd',
        'date_add',
    )
    search_fields = (
        'user',
    )
    fields = ('user', 'contacts', 'birth_date', 'genre', 'status')


class CommentaireAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'article',
        'user',
        'status',
        'date_add',
    )

    list_filter = (
        'status',
        'article',
        'user'
    )
    search_fields = (
        'message',
    )
    fieldsets = [
        ('Info ', {'fields': [
            'article',
            'message',
            'nom',
            'email',
            'website',
            'user'
        ]
        }),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'affiche_image',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'categorie',
        'status',
        'tags'
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': [
            'titre',
            'categorie',
            'tags',
            'contenu'
        ]
        }),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'sujet',
        'email',
        'status',
        'date_add',
    )

    list_filter = (
        'status',
    )
    search_fields = (
        'sujet',
    )
    fieldsets = [
        ('Info ', {'fields': [
            'nom',
            'email',
            'message',
            'sujet',
        ]
        }),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Profile, ProfileAdmin)
_register(models.Contact, ContactAdmin)
