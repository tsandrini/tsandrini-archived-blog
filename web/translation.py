from modeltranslation.translator import register, TranslationOptions
from web.entities.page import Page

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('content',)
