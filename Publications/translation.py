from modeltranslation.translator import translator, TranslationOptions
from .models import Publications

class PublicationsTranslator(TranslationOptions):
    fields = ('title','content','tags')

translator.register(Publications, PublicationsTranslator)
