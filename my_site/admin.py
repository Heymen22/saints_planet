from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *

admin.site.register(Catalog, DraggableMPTTAdmin)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Characteristic)
admin.site.register(CharacteristicValue)

# Register your models here.
