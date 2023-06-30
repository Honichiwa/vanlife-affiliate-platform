from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class VanConversion(models.Model):

    

    class Meta:
        verbose_name = _("van conversion")
        verbose_name_plural = _("van conversions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vanconversion_detail", kwargs={"pk": self.pk})
