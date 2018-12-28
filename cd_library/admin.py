from django.contrib import admin

# Register your models here.

# Let's register the CD model (or class) with the admin interface
from .models import CD
admin.site.register(CD)
