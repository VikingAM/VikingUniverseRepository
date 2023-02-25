from django.contrib import admin
from .models import types, industry_type, details, address_info, password_category, password_manager

# Register your models here.
admin.site.register(types)
admin.site.register(industry_type)
admin.site.register(details)
admin.site.register(address_info)
admin.site.register(password_category)
admin.site.register(password_manager)