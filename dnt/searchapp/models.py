from django.db import models


class History(models.Model):
    search_term = models.CharField(max_length=500, unique=False)

    def __str__(self):
        return self.search_term


class TranslationModel(models.Model):
    image_file = models.CharField(max_length=500, unique=True)
    translation = models.CharField(max_length=10000, unique=False, null=False)

    def __str__(self):
        return self.image_file + self.translation
