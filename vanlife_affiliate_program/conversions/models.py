from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class Conversion(models.Model):
    owner = models.ForeignKey(
        User, 
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name='cars',
        null=True, blank=True,
        db_index=True,
    )
    make = models.CharField(_("Make"), max_length=100)
    model = models.CharField(_("Model"), max_length=100)
    year = models.IntegerField(_("Year"))
    conversion_slug = models.SlugField(_("Conversion Slug"), null=False, blank=False, unique=True)
    side_picture = models.ImageField(_("side picture"), upload_to='conversions/')
    veichle_cost = models.IntegerField(_("Veichle cost"), null=True, blank=True)
    conversion_cost = models.IntegerField(_("Conversion cost"), null=True, blank=True)
    summary = models.TextField(_("Summary"), null=True, blank=True)
    interior1 = models.ImageField(_("Interior1"), upload_to='conversions/', null=True, blank=True)
    interior2 = models.ImageField(_("Interior2"), upload_to='conversions/', null=True, blank=True)
    interior3 = models.ImageField(_("Interior3"), upload_to='conversions/', null=True, blank=True)
    interior4 = models.ImageField(_("Interior4"), upload_to='conversions/', null=True, blank=True) 
    outro = models.TextField(_("outro"), null=True, blank=True)
    TYPE_CHOICES = (
        (0, _('Van')),
        (1, _('Rv')), 
    )
    c_type = models.PositiveBigIntegerField(
         _("ticket status"),
        choices=TYPE_CHOICES,
        db_index=True,
    )
    STATUS_CHOICES= (
        (0, _('Pending')),
        (1, _('Approved')),
        (2, _('Declined')),
    )
    verification_status = models.PositiveBigIntegerField(
        choices=STATUS_CHOICES,
        default=0,
        db_index=True,
    )
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    visible = models.BooleanField(_("visible"), default=True)

    class Meta:
        verbose_name = _("conversion")
        verbose_name_plural = _("conversions")

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse("conversion_detail", kwargs={"pk": self.pk})
    

class Social(models.Model):
    name = models.CharField(_("name"), max_length=100)
    svg_loggo_code = models.TextField(_("Font awesome logo svg"))
    
    class Meta:
        verbose_name = _("social")
        verbose_name_plural = _("socials")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("social_detail", kwargs={"pk": self.pk})


class ConversionSocial(models.Model):
    conversion = models.ForeignKey(
        Conversion, 
        verbose_name=_("conversion"), 
        on_delete=models.CASCADE,
        related_name='conversion_social'
    )
    social = models.ForeignKey(
        Social, 
        verbose_name=_("social"), 
        on_delete=models.CASCADE,
        related_name='conversion_social'
    )
    link = models.URLField(_("link"), max_length=200)
    

    class Meta:
        verbose_name = _("conversion social")
        verbose_name_plural = _("conversion socials")

    def __str__(self):
        return self.conversion

    def get_absolute_url(self):
        return reverse("conversionocial_detail", kwargs={"pk": self.pk})


class GadgetType(models.Model):
    name = models.CharField(_("name"), max_length=50)
    icon = models.ImageField(_("icon"), upload_to='gadgettypes/')
    
    class Meta:
        verbose_name = _("gadget type")
        verbose_name_plural = _("gadget types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gadgettype_detail", kwargs={"pk": self.pk})


class Gadget(models.Model):
    type = models.ForeignKey(
        GadgetType, 
        verbose_name=_("type"), 
        on_delete=models.CASCADE,
        related_name='gadget'
    )
    name = models.CharField(_("name"), max_length=100)
    picture = models.ImageField(_("picture"), upload_to='gadgets/')
    aff_link = models.URLField(_("affiliate link"), max_length=200)

    class Meta:
        verbose_name = _("gadget")
        verbose_name_plural = _("gadgets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gadget_detail", kwargs={"pk": self.pk})
