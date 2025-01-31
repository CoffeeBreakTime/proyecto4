from django.db import models


class Publicacion(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'publicacion'
        verbose_name = 'Publicacion'
        ordering = ["title"]

    def __str__(self):
        return self.title


class Noticias(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publicacion)

    class Meta:
        db_table = 'noticias'
        verbose_name = 'Noticias'
        ordering = ["headline"]

    def __str__(self):
        return self.headline
