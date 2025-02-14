from django.contrib import admin

# Register your models here.
from .models import Case,Catalog
# Register your models here.
admin.site.register(Case)
admin.site.register(Catalog)