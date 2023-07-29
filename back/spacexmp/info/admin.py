from django.contrib import admin
from .models import BannerCard, NavbarLink

class BannerCardAdmin(admin.ModelAdmin):
    list_display = ["top_text", "main_text", "bottom_text"]

class NavbarLinkAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]

admin.site.register(BannerCard, BannerCardAdmin)
admin.site.register(NavbarLink, NavbarLinkAdmin)
