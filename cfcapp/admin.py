from django.contrib import admin
from .models import SalesFormData
from django.http import HttpResponse, request
import import_export

class SalesDataModelResource(import_export.resources.ModelResource):

    class Meta:
        model = SalesFormData

class MyModelAdmin(admin.ModelAdmin):

    class SalesAdmin(import_export.admin.ImportExportModelAdmin):
        
        def get_queryset(self, request):
            qs = super(MyModelAdmin.SalesAdmin, self).get_queryset(request)
            print(request.user)
            if request.user.is_superuser:
                return SalesFormData.objects.all()
            else:
                return SalesFormData.objects.filter(sales_rep=request.user) 


        list_display = ['id', 'sales_rep', 'company_name', 'contact_email', 'office_phone_number', 'total_spent']
        search_fields = ['company_name', 'contact_email', 'office_phone_number']
        resource_class = SalesDataModelResource

        def get_fieldsets(self, request, obj=None):
            return(
                (None, {
                    'description': 'Contact Info',
                    'fields':   ('sales_rep','company_name', 'contact_name', 'contact_email', 'office_phone_number', 'direct_phone_number', 'total_spent', 'select_cities')
                }),
                ('Additional Info', {
                    'description': 'Additional Info',
                    'classes': ('collapse',),
                    'fields': ('address', 'city', 'province', 'postal_code','facebook_link', 'website_link', 'twitter_link')
                }),
                ('Toronto Fairs', {
                    'description': 'Toronto Booking Details',
                    'classes': ('collapse',),
                    'fields': ('toronto_dates', 'toronto_date_1', 'toronto_date_2','toronto_booth_options','toronto_additional_booth_option_1', 'toronto_additional_booth_option_2')
                }),
                ('Calgary Fairs', {
                    'description': 'Calgary Booking Details',
                    'classes': ('collapse',),
                    'fields': ('calgary_dates', 'calgary_date_1', 'calgary_date_2', 'calgary_date_3', 'calgary_booth_options', 'calgary_additional_booth_option_1', 'calgary_additional_booth_option_2','calgary_additional_booth_option_3', 'calgary_additional_lunch_option_1', 'calgary_additional_lunch_option_2','calgary_additional_lunch_option_3','calgary_options', 'calgary_diet_request_1', 'calgary_diet_request_2', 'calgary_diet_request_3', 'calgary_venue_options')
                }),
                ('Edmonton Fairs', {
                    'description': 'Edmonton Booking Details',
                    'classes': ('collapse',),
                    'fields': ('edmonton_dates', 'edmonton_date_1', 'edmonton_date_2', 'edmonton_date_3','edmonton_date_4', 'edmonton_booth_options', 'edmonton_additional_booth_option_1', 'edmonton_additional_booth_option_2','edmonton_additional_booth_option_3','edmonton_additional_booth_option_4', 'edmonton_additional_lunch_option_1', 'edmonton_additional_lunch_option_2','edmonton_additional_lunch_option_3','edmonton_additional_lunch_option_4','edmonton_additional_breakfast_option_1','edmonton_additional_breakfast_option_2','edmonton_additional_breakfast_option_3','edmonton_additional_breakfast_option_4', 'edmonton_diet_request_1', 'edmonton_diet_request_2','edmonton_diet_request_3','edmonton_diet_request_4','edmonton_venue_options')
                }),
                ('Winnipeg Fairs', {
                    'description': 'Calgary Booking Details',
                    'classes': ('collapse',),
                    'fields': ('winnipeg_dates', 'winnipeg_date_1', 'winnipeg_date_2', 'winnipeg_date_3', 'winnipeg_booth_options','winnipeg_additional_booth_option_1', 'winnipeg_additional_booth_option_2','winnipeg_additional_booth_option_3', 'winnipeg_additional_lunch_option_1','winnipeg_additional_lunch_option_2', 'winnipeg_additional_lunch_option_3', 'winnipeg_diet_request_1', 'winnipeg_diet_request_2', 'winnipeg_diet_request_3')
                })
            )

        def export_csv(modeladmin, request, queryset):
            import csv
            from django.utils.encoding import smart_str
            response = HttpResponse(content_type='text/csv')
            response['Content-Diposition'] = 'attachment; filename=mymodel.csv'
            writer = csv.writer(response, csv.excel)
            writer.writerow((
                smart_str(u"Order ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
                smart_str(u"Address"),
                smart_str(u"City Or Province"),
                smart_str(u"Postal Code"),
                smart_str(u"Contact Email"),
                smart_str(u"Office Phone"),
                smart_str(u"Direct Phone"),
                smart_str(u"Facebook Link"),
                smart_str(u"Website Link"),
                smart_str(u"Twitter Link"),
                smart_str(u"Select Cities"),
                smart_str(u"Toronto Dates"),
                smart_str(u"Toronto Booth Selection"),
                smart_str(u"Calgary Dates"),
                smart_str(u"Calgary Booth Selection"),
                smart_str(u"Edmonton Dates"),
                smart_str(u"Edmonton Booth Selection"),
                smart_str(u"Winnipeg Dates"),
                smart_str(u"Winnipeg Booth Selection")
            ))

            for obj in queryset:
                writer.writerow([
                    smart_str(obj.pk),
                    smart_str(obj.company_name),
                    smart_str(obj.contact_name),
                    smart_str(obj.address),
                    smart_str(obj.city_or_province),
                    smart_str(obj.postal_code),
                    smart_str(obj.contact_email),
                    smart_str(obj.office_phone_number),
                    smart_str(obj.direct_phone_number),
                    smart_str(obj.facebook_link),
                    smart_str(obj.website_link),
                    smart_str(obj.twitter_link),
                    smart_str(obj.select_cities),
                    smart_str(obj.toronto_dates),
                    smart_str(obj.toronto_booth_options),
                    smart_str(obj.calgary_dates),
                    smart_str(obj.calgary_booth_options),
                    smart_str(obj.edmonton_dates),
                    smart_str(obj.edmonton_booth_options),
                    smart_str(obj.winnipeg_dates),
                    smart_str(obj.winnipeg_booth_options)
            ])

            return response

        export_csv.short_description = u"Export Data"

        actions = [export_csv]


# Register your models here.
admin.site.register(SalesFormData, MyModelAdmin.SalesAdmin)