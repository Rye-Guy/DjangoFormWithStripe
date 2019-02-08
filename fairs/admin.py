from django.contrib import admin
from .models import TorontoFair, CalgaryFair, EdmontonFair, WinnipegFair
# Register your models here.
import import_export


class FairModelResource(import_export.resources.ModelResource):

    class Meta:
        model = TorontoFair


class FairAdmin(import_export.admin.ImportExportModelAdmin):

    list_display = ['id',  'get_related_company', 'date_selection', 'get_contact_name', 'get_office_phone' , 'get_contact_phone' ,'get_contact_email', 'fair_total_spent', 'related_sale']

    resource_class = FairModelResource

    def get_related_company(self, obj):
       try:
           return obj.related_sale.company_name

       except AttributeError: return 'No Attribute Found'
    get_related_company.short_description = 'Company Name'

    def get_total_spent(self, obj):
        try:
            return obj.related_sale.total_spent
        except AttributeError:
            return 'No Attribute Found'
    get_total_spent.short_description = 'Total Spent'

    def get_contact_name(self, obj):
        try:
            return obj.related_sale.contact_name
        except AttributeError:
            return 'No Attribute Found'

    get_contact_name.short_description = 'Contact Name'

    def get_contact_email(self, obj):
        try:
            return obj.related_sale.contact_email
        except AttributeError:
            return 'No Attribute Found'

    get_contact_email.short_description = 'Contact Email'

    def get_contact_phone(self, obj):
        try:
            return obj.related_sale.direct_phone_number
        except AttributeError:
            return 'No Attribute Found'

    get_contact_phone.short_description = 'Direct Line'

    def get_office_phone(self, obj):
        try:
            return obj.related_sale.office_phone_number
        except AttributeError:
            return 'No Attribute Found'

    get_office_phone.short_description = 'Office Line'


admin.site.register(TorontoFair, FairAdmin)
admin.site.register(CalgaryFair, FairAdmin)
admin.site.register(EdmontonFair, FairAdmin)
admin.site.register(WinnipegFair, FairAdmin)