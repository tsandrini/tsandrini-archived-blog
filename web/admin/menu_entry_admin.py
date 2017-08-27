from django.db import models
from django.utils.translation import ugettext as _
from django.contrib import admin
from web.entities import MenuEntry
from modeltranslation.admin import TranslationAdmin
from core.admin.actions import enable, disable
from django_ace import AceWidget as Ace

@admin.register(MenuEntry)
class MenuEntryAdmin(TranslationAdmin):
    fields = (
        ('slug'),
        ('parent', 'position')
    )
    search_fields = ('slug',)
    list_display = ('__str__', 'enabled')
    actions = (enable, disable)
