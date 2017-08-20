from modeltranslation.translator import register, TranslationOptions
from .entities.page import Page

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('content',)
