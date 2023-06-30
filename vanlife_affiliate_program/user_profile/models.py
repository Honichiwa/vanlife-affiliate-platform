from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.forms import RadioSelect

class ProfileIcon(models.Model):
    name = models.CharField(_("name"), max_length=50)
    icon = models.ImageField(_("icon"), upload_to="profile/profileicons")
    
    class Meta:
        verbose_name = _("profile icon")
        verbose_name_plural = _("profile icons")

    def __str__(self):
        return mark_safe(f'<img src="{self.icon.url}" alt="{self.name}" width="32" height="32" />{self.name}')

    def get_absolute_url(self):
        return reverse("profileicon_detail", kwargs={"pk": self.pk})
    
class ProfileReason(models.Model):
    statment = models.TextField(_("statment"))

    class Meta:
        verbose_name = _("profile reason")
        verbose_name_plural = _("profile reasons")

    def __str__(self):
        return self.statment

    def get_absolute_url(self):
        return reverse("reason_detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(),
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='profile',
        null=True, blank=True,
    )
    icon = models.ForeignKey(
        ProfileIcon,
        verbose_name=_("icon"), 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name='profiles',
        limit_choices_to={'name__isnull': False}
    )
    about_you = models.TextField(
        _("about you"),
        null=True, blank=True
    )
    reason = models.ForeignKey(
        ProfileReason, 
        verbose_name=_("reason"),
        related_name='profiles',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
         return f'{str(self.user)}'

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    
    
    def is_complete(self):
        required_fields = ['about_you', 'reason', 'icon',]

        for field in required_fields:
            if not getattr(self, field):
                return False

        return True