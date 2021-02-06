from django.contrib import admin

# Register your models here.
from .models import Basic,Family

admin.site.register(Basic)
admin.site.register(Family)

