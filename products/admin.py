from django.contrib import admin
from .models import Product,Kids,Women,Men,Unisex,Cart


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')


class KidsAdmin(admin.ModelAdmin):
    list_display=('kname','kprice','kstock')

class WomenAdmin(admin.ModelAdmin):
    list_display=('wname','wprice','wstock')

class MenAdmin(admin.ModelAdmin):
    list_display=('mname','mprice','mstock')

class UnisexAdmin(admin.ModelAdmin):
    list_display=('uname','uprice','ustock')

class CartAdmin(admin.ModelAdmin):
    list_display=('cname',)


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Kids,KidsAdmin)
admin.site.register(Women,WomenAdmin)
admin.site.register(Men,MenAdmin)
admin.site.register(Unisex,UnisexAdmin)
admin.site.register(Cart,CartAdmin)