from django.contrib import admin
from . models import *
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html


class AuthorAdmin(TranslationAdmin):
    list_display = ['author', 'slug', 'discription']
    prepopulated_fields = {'slug': ('author',)}

    class Meta:
        model = Author

admin.site.register(Author, AuthorAdmin)

class EpochAdmin(TranslationAdmin):
    list_display = ['epoch', 'slug', 'discription']
    prepopulated_fields = {'slug': ('epoch',)}

    class Meta:
        model = Epoch

admin.site.register(Epoch, EpochAdmin)

class PictureAdmin(TranslationAdmin):

	def image_tag(self, obj):
		return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

	list_display = ['title', 'slug', 'epoch', 'status', 'image_tag'] #
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title',)
	list_filter = ['epoch', 'author', 'status', 'publish']
	data_hierachy = 'publish'
	ordering = ['status', '-publish']

	class Meta:
		model = Picture

admin.site.register(Picture, PictureAdmin)
