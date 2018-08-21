from django.contrib import admin

# Register your models here.


from mainapp.models import *



admin.site.register(Camp)
admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(Districts)
admin.site.register(Locality)