from django.contrib import admin
from .models import Application, AppLogs


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('date', 'phone', 'product', 'decision')
    list_filter = ('product', 'decision')
    search_fields = ('date', 'phone')
    ordering = ('date', 'phone')

    fields = ('date', 'product', 'phone', 'decision', 'comment', 'version')
    readonly_fields = ('date', 'version')


class AppLogsAdmin(admin.ModelAdmin):
    list_display = ('app_id', 'date', 'phone', 'product', 'decision')

    fields = ('app_id', 'date', 'product', 'phone', 'decision', 'comment')
    readonly_fields = ('date', )


admin.site.register(Application, ApplicationAdmin)
admin.site.register(AppLogs, AppLogsAdmin)
