from modeltranslation.translator import register, TranslationOptions
from web.entities import Page, MenuEntry

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('content',)

@register(MenuEntry)
class MenuEntryTranslationOptions(TranslationOptions):
    fields = ('slug',)
