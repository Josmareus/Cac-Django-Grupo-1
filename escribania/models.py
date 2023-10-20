from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ActoJuridico(models.Model):
    nombre=models.CharField(max_length=150)

    class Meta:
        ordering = ['nombre']

    def get_absolute_url(self):
        return reverse("act-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)


class Escribano(models.Model):

    class caracterChoices(models.TextChoices):
        TITU='Titular', _('Titular')
        ADSC='Adscripto', _('Adscripto')

    escribano=models.CharField(max_length=150)
    caracter = models.CharField(
        max_length=50,
        choices=caracterChoices.choices,
        default=caracterChoices.TITU,
        verbose_name="Carácter"
    )
    actos_juridicos=models.ManyToManyField(ActoJuridico, through="ActoEscribano",blank=True, verbose_name="Actos Jurídicos")

    class Meta:
        ordering = ['escribano']

    def get_absolute_url(self):
        return reverse("clerk-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.pk, self.escribano)


class Escritura(models.Model):
    fecha=models.DateField(verbose_name="Fecha de Escritura")
    escribano=models.ForeignKey(Escribano, on_delete=models.CASCADE, null=True, blank=True)
    folio=models.SmallIntegerField(null=True, blank=True)
    acto=models.ForeignKey(ActoJuridico, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Acto Jurídico")
    otorgante=models.CharField(max_length=300)
    aceptante=models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("document-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.fecha, self.aceptante)


class ActoEscribano(models.Model):
    acto=models.ForeignKey(ActoJuridico,on_delete=models.CASCADE,null=True,blank=True, verbose_name="Acto Jurídico")
    escribano=models.ForeignKey(Escribano,on_delete=models.CASCADE,null=True,blank=True, verbose_name="Escribano")