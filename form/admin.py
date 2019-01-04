from django.contrib import admin
from .models import SalesFormData
from django.http import HttpResponse, request

class MyModelAdmin(admin.ModelAdmin):

    def export_csv(modeladmin, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Diposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)
        writer.writerow([
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
        ])

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
admin.site.register(SalesFormData, MyModelAdmin)
