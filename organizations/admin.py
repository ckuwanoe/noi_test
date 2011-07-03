from organizations.models import Organization
from organizations.models import Person
from organizations.models import Internal
from django.contrib import admin

class PersonInline(admin.TabularInline):
    model = Person
    extra = 0

class InternalInline(admin.TabularInline):
    model = Internal
    extra = 0    
    
class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Organization', {'fields': ['name', 'founded_date', 'legal_status', 'number_staff', 'contact_person']}),
    ]
    inlines = [PersonInline, InternalInline]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person)
admin.site.register(Internal)