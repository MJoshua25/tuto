from django.db import models


# Create your models here.

class Categorie(models.Model):
    titre = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='categories')

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return str(self.titre)


class Tag(models.Model):
    titre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return str(self.titre)


# TODO: article Paul

# TODO: commentaire Daouda