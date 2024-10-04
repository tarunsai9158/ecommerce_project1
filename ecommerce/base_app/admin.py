from django.contrib import admin
from base_app.models import *



class CategoryAdmin(admin.ModelAdmin):
  list_display=('id','Category_name')


class ProductAdmin(admin.ModelAdmin):
  list_display=('id','category','name','description','price','image')

class FeedbackAdmin(admin.ModelAdmin):
  list_display=('name','email','feedback')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
