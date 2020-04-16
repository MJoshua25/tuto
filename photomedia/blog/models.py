from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import HTMLField


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
    date_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_upd = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return str(self.titre)


# TODO: article Paul

# TODO: commentaire Daouda, admin Tag


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contacts = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True)
    genre = models.CharField(max_length=30, null=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_upd = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.BooleanField(default=True, null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user.username)


class Article(models.Model):
    titre = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='articles')
    contenu = HTMLField('Content')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self) -> str:
        return str(self.titre)


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    message = models.TextField()
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    website = models.URLField()
    pseudo = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self) -> str:
        return '{}  -  {}'.format(self.pseudo, self.message)
