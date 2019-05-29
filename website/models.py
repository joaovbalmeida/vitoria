from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField("Nome", max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['id',]

    def __str__(self):
        return self.name

class Content(models.Model):
    page = models.ForeignKey(Page, on_delete=models.PROTECT, verbose_name="Página", related_name="contents")
    key = models.CharField("Nome", max_length=255)
    text = models.TextField("Texto", null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        ordering = ['id',]

    def __str__(self):
        return self.key

class PartnersLogos(models.Model):
    name = models.CharField("Nome", max_length=255, null=True, blank=True)
    logo = models.ImageField("Logo", upload_to='partnerslogos/%Y/%m/%d/', max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Logo do Parceiro'
        verbose_name_plural = 'Logos dos Parceiros'