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
    search_fields = ['date_selection']
    list_display = ['id', 'date_selection', 'get_related_company', 'get_contact_name', 'get_office_phone' , 'get_contact_email', 'package_type',  'get_discount_percentage', 'booth_cost','get_related_sales_rep', 'special_request']

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

    def get_discount_percentage(self, obj):
        try:
            return obj.related_sale.discount_percentage
        except AttributeError:
            return 'No Attribute Found'
    get_discount_percentage.short_description = 'Discounted'



    def export_genral_csv(modeladmin, request, queryset):

        def get_related_contact_info(obj):
            try:
                contact = obj.contact.all()
                return [contact[0].name, contact[0].phone_number, contact[0].email]
            except IndexError:
                return [obj.related_sale.contact_name, obj.related_sale.office_phone_number, obj.related_sale.contact_email]

        response = HttpResponse(content_type='text/csv')
        response['Content-Diposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)

        exporting_city = queryset[0].related_class()

        if exporting_city == 'toronto':
            writer.writerow((
                smart_str(u"Booth ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
                smart_str(u"Telephone"),
                smart_str(u"Email"),
                smart_str(u"Owner"),
                smart_str(u"Sponsorship Level"),
                smart_str(u"Notes")
            ))

        if exporting_city == 'edmonton':
            writer.writerow((
                smart_str(u"Booth ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
                smart_str(u"Telephone"),
                smart_str(u"Email"),
                smart_str(u"Owner"),
                smart_str(u"Sponsorship Level"),
                smart_str(u"Extra Lunch"),
                smart_str(u"Extra Breakfast"),
                smart_str(u"Wifi"),
                smart_str(u"Electricity"),
                smart_str(u"Notes")
            ))

        if exporting_city == 'calgary':
            writer.writerow((
                smart_str(u"Booth ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
                smart_str(u"Telephone"),
                smart_str(u"Email"),
                smart_str(u"Owner"),
                smart_str(u"Sponsorship Level"),
                smart_str(u"Extra Lunch"),
                smart_str(u"Wifi"),
                smart_str(u"Electricity"),
                smart_str(u"Notes")
            ))

        if exporting_city == 'winnipeg':
            writer.writerow((
                smart_str(u"Booth ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
                smart_str(u"Telephone"),
                smart_str(u"Email"),
                smart_str(u"Owner"),
                smart_str(u"Sponsorship Level"),
                smart_str(u"Extra Lunch"),
                smart_str(u"Notes")
            ))


        for obj in queryset:
            theContact = get_related_contact_info(obj)

            if exporting_city == 'toronto':
                writer.writerow([
                    smart_str(obj.booth_id),
                    smart_str(obj.related_sale.company_name),
                    smart_str(theContact[0]),
                    smart_str(theContact[1]),
                    smart_str(theContact[2]),
                    smart_str(obj.related_sale.sales_rep),
                    smart_str(obj.package_type),
                    smart_str(obj.special_request)
                ])

            if exporting_city == 'edmonton':
                writer.writerow([
                    smart_str(obj.booth_id),
                    smart_str(obj.related_sale.company_name),
                    smart_str(theContact[0]),
                    smart_str(theContact[1]),
                    smart_str(theContact[2]),
                    smart_str(obj.related_sale.sales_rep),
                    smart_str(obj.package_type),
                    smart_str(obj.additional_lunch_option),
                    smart_str(obj.additional_breakfast_option),
                    smart_str(obj.wifi),
                    smart_str(obj.electricity),
                    smart_str(obj.special_request)

                ])

            if exporting_city == 'calgary':
                writer.writerow([
                    smart_str(obj.booth_id),
                    smart_str(obj.related_sale.company_name),
                    smart_str(theContact[0]),
                    smart_str(theContact[1]),
                    smart_str(theContact[2]),
                    smart_str(obj.related_sale.sales_rep),
                    smart_str(obj.package_type),
                    smart_str(obj.additional_lunch_option),
                    smart_str(obj.wifi),
                    smart_str(obj.electricity),
                    smart_str(obj.special_request)
                ])

            if exporting_city == 'winnipeg':
                writer.writerow([
                    smart_str(obj.booth_id),
                    smart_str(obj.related_sale.company_name),
                    smart_str(theContact[0]),
                    smart_str(theContact[1]),
                    smart_str(theContact[2]),
                    smart_str(obj.related_sale.sales_rep),
                    smart_str(obj.package_type),
                    smart_str(obj.additional_lunch_option),
                    smart_str(obj.special_request)
                ])

        return response

    export_genral_csv.short_description = u"Export All Fair Data"


    def fair_specific_csv(modeladmin, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Diposition'] = 'attachment; filename=relateddata.csv'
        writer = csv.writer(response, csv.excel)



        writer.writerow((
            smart_str(u"ID"),
            smart_str(u"Company Name"),
            smart_str(u"Contact Name"),
            smart_str(u"Phone Numbers"),
            smart_str(u"Email"),
        ))
        for obj in queryset:
            all_contacts = obj.contact.all()
            for contact in all_contacts:
                writer.writerow([
                    smart_str(contact.id),
                    smart_str(obj.related_sale.company_name),
                    smart_str(contact.name),
                    smart_str(contact.phone_number),
                    smart_str(contact.email),

                ])

        return response


    fair_specific_csv.short_description = u"All Fair Contacts"

    actions = [export_genral_csv, fair_specific_csv]

class ContactAdmin(import_export.admin.ImportExportModelAdmin):

    class Meta:
        model = OnSiteContacts

    exclude = ['toronto_fairs', 'edmonton_fairs', 'calgary_fairs', 'winnipeg_fairs']

admin.site.register(TorontoFair, FairAdmin)
admin.site.register(CalgaryFair, FairAdmin)
admin.site.register(EdmontonFair, FairAdmin)
admin.site.register(WinnipegFair, FairAdmin)
admin.site.register(OnSiteContacts, ContactAdmin)
