from django.contrib import admin

from jurnal.models import Obs, ObsType


class ObsAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['question']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    list_display = ('date', 'category', 'user', 'content')
    list_filter = ['date', 'category', 'user']
    search_fields = ['date']
    date_hierarchy = 'date'


class ObsTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Obs, ObsAdmin)
admin.site.register(ObsType, ObsTypeAdmin)
