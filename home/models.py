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


class Atliktas_Darbas(models.Model):

    class Meta:
        verbose_name_plural = 'Atlikti Darbai'

    bendrija = models.ForeignKey(Bendrija, on_delete=models.CASCADE,
                                 related_name="atliktas_darbas")
    pavadinimas = models.CharField(max_length=254)
    aprasymas = models.CharField(max_length=254, null=True, blank=True)
    preliminari_kaina = models.CharField(max_length=254)
    galutine_kaina = models.CharField(max_length=254, null=True, blank=True)
    atlikti_iki = models.DateField()
    darbas_atlikas = models.DateField(null=True, blank=True)
    pastabos = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.pavadinimas
