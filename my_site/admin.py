from django.contrib import admin
from .models import *

admin.site.register(Catalog)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Characteristic)
admin.site.register(CharacteristicValue)

# Register your models here.
