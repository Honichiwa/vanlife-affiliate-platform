from django.contrib import admin
from . import models

admin.site.register(models.Conversion)
admin.site.register(models.Social)
admin.site.register(models.ConversionSocial)
admin.site.register(models.Gadget)
admin.site.register(models.GadgetType)