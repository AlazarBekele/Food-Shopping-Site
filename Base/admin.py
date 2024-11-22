from django.contrib import admin
from .models import (
    Category,
    Index,
    Index_page_image,
    x_icon_Dynamic
)
# Register your models here.

admin.site.register (Category)
admin.site.register (Index)
admin.site.register (Index_page_image)
admin.site.register (x_icon_Dynamic)