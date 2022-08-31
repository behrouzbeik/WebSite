from django.contrib import admin
from .models import *
# Register your models here.
class ProductVariantsinLines(admin.TabularInline):
    model = Variants
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update')
    prepopulated_fields = {
        'slug' : ('name',)
    }

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','create','update' , 'amount' , 'available' , 'unit_price' , 'discount' , 'total_price']
    inlines = [ProductVariantsinLines]
    list_editable = ('amount',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','create','rate')



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Variants)
admin.site.register(Comment,CommentAdmin)