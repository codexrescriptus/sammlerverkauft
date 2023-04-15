from modeltranslation.translator import translator, TranslationOptions
from . models import Author, Epoch, Picture

class AuthorTranslationOptions(TranslationOptions):
    fields = ('author', 'discription')

translator.register(Author, AuthorTranslationOptions)

class EpochTranslationOptions(TranslationOptions):
    fields = ('epoch', 'discription')

translator.register(Epoch, EpochTranslationOptions)

class PictureTranslationOptions(TranslationOptions):
    fields = ('title', 'author', 'epoch', 'country')

translator.register(Picture, PictureTranslationOptions)