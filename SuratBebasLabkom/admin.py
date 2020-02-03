from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    pass


admin.site.register(DataSuratBebasLabkom, PostAdmin)
