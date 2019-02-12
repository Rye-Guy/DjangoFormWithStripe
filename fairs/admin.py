from django.contrib import admin
from .models import TorontoFair, CalgaryFair, EdmontonFair, WinnipegFair, OnSiteContacts
from django.http import HttpResponse, request

# Register your models here.
import import_export
import csv
from django.utils.encoding import smart_str

class FairModelResource(import_export.resources.ModelResource):

    class Meta:
        model = CalgaryFair


class FairAdmin(import_export.admin.ImportExportModelAdmin):

    list_display = ['id', 'date_selection', 'get_related_company', 'get_contact_name', 'get_office_phone' , 'get_contact_email', 'booth_option', 'get_related_sales_rep', 'special_request']

    resource_class = FairModelResource

    def get_related_company(self, obj):
       try:
           return obj.related_sale.company_name

       except AttributeError: return 'No Attribute Found'
    get_related_company.short_description = 'Company Name'

    def get_related_sales_rep(self, obj):
        try:
            return obj.related_sale.sales_rep
        except AttributeError: return 'No Attribute Found'

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


    def export_genral_csv(modeladmin, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Diposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)


        writer.writerow((

        ))

        for obj in queryset:

            writer.writerow([

            ])

            return response
        export_csv.short_description = u"Export All Data"


    def fair_specific_csv(modeladmin, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Diposition'] = 'attachment; filename=relateddata.csv'
        writer = csv.writer(response, csv.excel)


        print(queryset)

        writer.writerow((
            smart_str(u"Order ID"),
            smart_str(u"Company Name"),
            smart_str(u"Additional Lunches"),
            smart_str(u"Power"),
            smart_str(u"Electricity"),
            smart_str(u"Special Notes")
        ))
        for obj in queryset:

            writer.writerow([
                smart_str(obj.pk),
                smart_str(obj.related_sale.company_name),
                smart_str(obj.additional_lunch_option),
                smart_str(obj.wifi),
                smart_str(obj.electricity),
                smart_str(obj.special_request)
            ])

        return response

        export_csv.short_description = u"Export Related Data"

    actions = [export_genral_csv, fair_specific_csv]

admin.site.register(TorontoFair, FairAdmin)
admin.site.register(CalgaryFair, FairAdmin)
admin.site.register(EdmontonFair, FairAdmin)
admin.site.register(WinnipegFair, FairAdmin)
admin.site.register(OnSiteContacts)