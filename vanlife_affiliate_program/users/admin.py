from django.contrib import admin
from .models import CustomUser, ProfileIcon, ProfileReason

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ProfileIcon)
admin.site.register(ProfileReason)