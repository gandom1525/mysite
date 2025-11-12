from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title',)
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    ordering = ['id'] #-
    search_fields = ['name','massage']


admin.site.register(Contact,ContactAdmin)

# Register your models here.
