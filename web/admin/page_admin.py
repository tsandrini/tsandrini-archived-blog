from django.db import models
from django.utils.translation import ugettext as _
from django.contrib import admin
from web.entities import Page
from modeltranslation.admin import TranslationAdmin
from core.admin.actions import enable, disable
from django_ace import AceWidget as Ace

@admin.register(Page)
class PageAdmin(TranslationAdmin):
    fields = (
        ('identifier', 'enabled'),
        ('template_path', 'dynamic_handling'),
        ('menu_entry', 'dynamic_content'),
        ('content')
    )
    formfield_overrides = {
        models.TextField: {
            'widget': Ace(
                mode='django',
                theme='monokai',
                wordwrap=True,
                showprintmargin=True,
                width='650px'
            )
        }
    }
    search_fields = ('identifier')
    list_display = ('__str__', 'dynamic_content', 'dynamic_handling', 'enabled')
    actions = (enable, disable)

    class Media:
        js = (
            'js/admin/entities/page.js',
        )
