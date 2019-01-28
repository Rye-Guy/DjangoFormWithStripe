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


class FairModelResource(import_export.resources.ModelResource):

    class Meta:
        model = TorontoFair


class FairAdmin(import_export.admin.ImportExportModelAdmin):
    list_display = ['id', 'related_sale', 'related_sale_id']
    list_select_related = ['related_sale']
    #list_display += ('toronto_booking_id', 'get_related_bookings_toronto')
    search_fields = ['related_sale__id']
    resource_class = FairModelResource





# Register your models here.
admin.site.register(SalesFormData, MyModelAdmin.SalesAdmin)
admin.site.register(TorontoFair, FairAdmin)
admin.site.register(CalgaryFair, FairAdmin)
admin.site.register(EdmontonFair, FairAdmin)
admin.site.register(WinnipegFair, FairAdmin)