from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('date', 'phone', 'product', 'decision')
    list_filter = ('product', 'decision')
    search_fields = ('date', 'phone')
    ordering = ('date', 'phone')

    fields = ('date', 'product', 'phone', 'decision', 'comment')
    readonly_fields = ('date', )


admin.site.register(Application, ApplicationAdmin)