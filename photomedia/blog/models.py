from django.db import models


# Create your models here.

class Categorie(models.Model):
    titre = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='categories')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Une categorie"
        verbose_name_plural = "Les categories"

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

# TODO: commentaire Daouda, admin Tag