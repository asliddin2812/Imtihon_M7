from modeltranslation.translator import translator, TranslationOptions
from .models import Paper

class PapersTranslator(TranslationOptions):
    fields = ('title','author','description')

translator.register(Paper, PapersTranslator)
