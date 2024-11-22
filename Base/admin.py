from django.contrib import admin
from .models import (
    Category,
    index,
    index_page_image
)
# Register your models here.

admin.site.register (Category)
admin.site.register (index)
admin.site.register (index_page_image)