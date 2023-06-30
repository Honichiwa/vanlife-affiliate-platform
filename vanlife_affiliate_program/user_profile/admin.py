from django.contrib import admin
from . models import ProfileIcon, Profile, ProfileReason

class ProfileIconAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

admin.site.register(ProfileIcon, ProfileIconAdmin)
admin.site.register(Profile)
admin.site.register(ProfileReason)