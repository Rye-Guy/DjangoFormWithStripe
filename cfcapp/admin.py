from django.contrib import admin
from .models import SalesFormData
from fairs.models import TorontoFair, CalgaryFair, EdmontonFair, WinnipegFair
from django.http import HttpResponse, request
import import_export


class SalesDataModelResource(import_export.resources.ModelResource):

    class Meta:
        model = SalesFormData

class MyModelAdmin(admin.ModelAdmin):

    class SalesAdmin(import_export.admin.ImportExportModelAdmin):

        admin.AdminSite.site_header = 'Career Fair Canada Admin'
        admin.AdminSite.site_title = 'Career Fair | Admin'
        admin.AdminSite.index_title = 'Career Fair Canada Admin'

        def get_queryset(self, request):
            qs = super(MyModelAdmin.SalesAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return SalesFormData.objects.select_related()
            else:
                return SalesFormData.objects.filter(sales_rep=request.user) 


        list_display = ['id', 'sales_rep', 'company_name', 'office_phone_number', 'total_spent', 'select_cities']
        search_fields = ['company_name', 'contact_email', 'office_phone_number', 'toronto_booking_id']
        resource_class = SalesDataModelResource
        list_display += ('toronto_booking_id', 'get_related_bookings_toronto')
        list_display += ('calgary_booking_id', 'get_related_bookings_calgary')
        list_display += ('edmonton_booking_id', 'get_related_bookings_edmonton')
        list_display += ('winnipeg_booking_id', 'get_related_bookings_winnipeg')


        def get_related_bookings_toronto(self, obj):
            try:
                return obj.toronto_booking.toronto_dates, obj.toronto_booking.toronto_booth_options

            except AttributeError:
                return obj.toronto_booking
        get_related_bookings_toronto.short_description = 'Toronto Details'

        def get_related_bookings_calgary(self, obj):
            try:
                return obj.calgary_booking.calgary_dates, obj.calgary_booking.calgary_booth_options

            except AttributeError:
                return obj.calgary_booking
        get_related_bookings_calgary.short_description = 'Calgary Details'

        def get_related_bookings_edmonton(self, obj):
            try:
                return obj.edmonton_booking.edmonton_dates, obj.edmonton_booking.edmonton_booth_options

            except AttributeError:
                return obj.edmonton_booking
        get_related_bookings_edmonton.short_description = 'edmonton Details'

        def get_related_bookings_winnipeg(self, obj):
            try:
                return obj.winnipeg_booking.winnipeg_dates, obj.winnipeg_booking.winnipeg_booth_options

            except AttributeError:
                return obj.winnipeg_booking

        get_related_bookings_winnipeg.short_description = 'winnipeg Details'

        def export_csv(modeladmin, request, queryset):
            import csv
            from django.utils.encoding import smart_str
            response = HttpResponse(content_type='text/csv')
            response['Content-Diposition'] = 'attachment; filename=mymodel.csv'
            writer = csv.writer(response, csv.excel)

            def get_attributes_of_forgien_key_obj(obj, key):
                try:
                    if key == 'toronto':
                        try:
                            obj = obj.toronto_booking
                            return obj, obj.toronto_dates, obj.toronto_date_1, obj.toronto_date_2, obj.toronto_booth_option_1, obj.toronto_booth_option_2, obj.toronto_additional_booth_option_1, obj.toronto_additional_booth_option_2
                        except AttributeError:
                            return ['-', '-', '-', '-', '-', '-', '-', '-']
                    elif key == 'calgary':
                        try:
                            obj = obj.calgary_booking
                            return obj, obj.calgary_dates, obj.calgary_booth_option_1, obj.calgary_booth_option_2, obj.calgary_booth_option_3, obj.calgary_options, obj.calgary_date_1, obj.calgary_date_2, obj.calgary_date_3, obj.calgary_additional_booth_option_1, obj.calgary_additional_booth_option_2, obj.calgary_additional_booth_option_3, obj.calgary_additional_lunch_option_1, obj.calgary_additional_lunch_option_2, obj.calgary_additional_lunch_option_3, obj.calgary_diet_request_1, obj.calgary_diet_request_2, obj.calgary_diet_request_3, obj.calgary_venue_options
                        except AttributeError:
                            return ['-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-']
                    elif key == 'edmonton':
                        try:
                            pass
                        except AttributeError:
                            return ['']

                except AttributeError:
                    return None



            writer.writerow((
                smart_str(u"Order ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
                smart_str(u"Toronto Fair"),
                smart_str(u"TO Fair Dates"),
                smart_str(u"TO Date 1"),
                smart_str(u"TO Date 2"),
                smart_str(u"TO Booth Option 1"),
                smart_str(u"TO Booth Option 2"),
                smart_str(u"TO Additional Booth 1"),
                smart_str(u"TO Additional Booth 2"),
                smart_str(u"Calgary Fair"),
                smart_str(u"CAL Fair Dates"),
                smart_str(u"CAL Booth Option 1"),
                smart_str(u"CAL Booth Option 2"),
                smart_str(u"CAL Booth Option 3"),
                smart_str(u"CAL Options"),
                smart_str(u"CAL Date 1"),
                smart_str(u"CAL Date 2"),
                smart_str(u"CAL Date 3"),
                smart_str(u"CAL Additional Booth 1"),
                smart_str(u"CAL Additional Booth 2"),
                smart_str(u"CAL Additional Booth 3"),
                smart_str(u"CAL Additional Lunch 1"),
                smart_str(u"CAL Additional Lunch 2"),
                smart_str(u"CAL Additional Lunch 3"),
                smart_str(u"CAL Diet Request 1"),
                smart_str(u"CAL Diet Request 2"),
                smart_str(u"CAL Diet Request 3"),
                smart_str(u"CAL Venue Options"),
                smart_str(u"Edmonton Fair"),
                smart_str(u"Winnipeg Fair")

            ))



            for obj in queryset:
                torontoAttrs = get_attributes_of_forgien_key_obj(obj, 'toronto')
                calgaryAttrs = get_attributes_of_forgien_key_obj(obj, 'calgary')
                for index in range(0, len(calgaryAttrs)):
                    print(index, calgaryAttrs[index])

                writer.writerow([
                    smart_str(obj.pk),
                    smart_str(obj.company_name),
                    smart_str(obj.contact_name),
                    smart_str(torontoAttrs[0]),
                    smart_str(torontoAttrs[1]),
                    smart_str(torontoAttrs[2]),
                    smart_str(torontoAttrs[3]),
                    smart_str(torontoAttrs[4]),
                    smart_str(torontoAttrs[5]),
                    smart_str(torontoAttrs[6]),
                    smart_str(torontoAttrs[7]),
                    smart_str(calgaryAttrs[0]),
                    smart_str(calgaryAttrs[1]),
                    smart_str(calgaryAttrs[2]),
                    smart_str(calgaryAttrs[3]),
                    smart_str(calgaryAttrs[4]),
                    smart_str(calgaryAttrs[5]),
                    smart_str(calgaryAttrs[6]),
                    smart_str(calgaryAttrs[7]),
                    smart_str(calgaryAttrs[8]),
                    smart_str(calgaryAttrs[9]),
                    smart_str(calgaryAttrs[10]),
                    smart_str(calgaryAttrs[11]),
                    smart_str(calgaryAttrs[12]),
                    smart_str(calgaryAttrs[13]),
                    smart_str(calgaryAttrs[14]),
                    smart_str(calgaryAttrs[15]),
                    smart_str(calgaryAttrs[16]),
                    smart_str(calgaryAttrs[17]),
                    smart_str(calgaryAttrs[18]),

                    smart_str(obj.edmonton_booking),
                    smart_str(obj.winnipeg_booking),


            ])

            return response

        export_csv.short_description = u"Export All Data"

        actions = [export_csv]

# Register your models here.
admin.site.register(SalesFormData, MyModelAdmin.SalesAdmin)
