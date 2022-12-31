from django.db import models
import datetime


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


class Ataskaita(models.Model):

    class Meta:
        verbose_name_plural = 'Ataskaitos'

    MENESIAI = (
        ('Sausis', 'Sausis'),
        ('Vasaris', 'Vasaris'),
        ('Kovas', 'Kovas'),
        ('Balandis', 'Balandis'),
        ('Gegužė', 'Gegužė'),
        ('Birželis', 'Birželis'),
        ('Liepa', 'Liepa'),
        ('Rugpjutis', 'Rugpjutis'),
        ('Rugsėjis', 'Rugsėjis'),
        ('Spalis', 'Spalis'),
        ('Lapkritis', 'Lapkritis'),
        ('Gruodis', 'Gruodis'),
    )

    bendrija = models.ForeignKey(Bendrija, on_delete=models.CASCADE,
                                 related_name="ataskaita")
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    mėnesis = models.CharField(null=False, blank=False, choices=MENESIAI, max_length=20)
    atlyginimas = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    sodra = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vmi = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    pvm_saskaitos_kvitas = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    bankines_operacijos = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f"{self.year} , {self.mėnesis}"

    @property
    def sum(self):
        return sum([self.atlyginimas, self.sodra, self.vmi, self.pvm_saskaitos_kvitas, self.bankines_operacijos])
