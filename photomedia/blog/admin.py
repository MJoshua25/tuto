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
    

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Tag, TagAdmin)
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
    fields=('user','contacts','birth_date','genre','status','date_upd','date_add',)
    
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)

class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'message',
        'pseudo',
        'status',
        'date_add',
    )

    list_filter = (
        'status',
        'date_add',
        'message',
    )
    search_fields = (
        'pseudo',
    )
    fields=('message','pseudo','status','date_upd',)
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Commentaire, CommentaireAdmin)



class ArticleAdmin(admin.ModelAdmin):

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
    #readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        #('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))
    
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)