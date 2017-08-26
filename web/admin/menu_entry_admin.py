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
        ('slug_cs', 'slug_en'),
        ('parent', 'position')
    )
    list_display = ['enabled']
    actions = [enable, disable]
