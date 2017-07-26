from django.contrib import admin

# Register your models here.
from .models import Product, Application, Home, Contact
admin.site.register(Product)
admin.site.register(Application)
admin.site.register(Home)
admin.site.register(Contact)