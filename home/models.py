from django.db import models


class Bendrija(models.Model):

    class Meta:
        verbose_name_plural = 'Bendrijos'

    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.address
