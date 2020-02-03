from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'waktu_posting']
    pass


admin.site.register(Post, PostAdmin)
