from django.contrib import admin
from .models import SalesFormData
from fairs.models import TorontoFair, CalgaryFair, EdmontonFair, WinnipegFair
from django.http import HttpResponse, request
from django.db.models import Prefetch
from django.core.exceptions import ObjectDoesNotExist
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

        filter_horizontal = ['toronto_booking', 'winnipeg_booking', 'edmonton_booking', 'calgary_booking']
        list_display = ['id', 'sales_rep', 'company_name', 'office_phone_number', 'subtotal', 'discount_amount', 'discount_percentage', 'total_spent',  'select_cities']
        search_fields = ['company_name', 'contact_email', 'office_phone_number']
        resource_class = SalesDataModelResource


        def export_csv(modeladmin, request, queryset):
            import csv
            from django.utils.encoding import smart_str
            response = HttpResponse(content_type='text/csv')
            response['Content-Diposition'] = 'attachment; filename=mymodel.csv'
            writer = csv.writer(response, csv.excel)




            def get_attributes_of_forgien_key_obj(obj, key):
                #try:
                    if key == 'toronto':
                        try:
                            obj_id = obj.id
                            related_data_qs = TorontoFair.objects.all().filter(related_sale=obj_id)
                            values = []
                            for index in range(0, 3):
                                print(related_data_qs)
                                try:
                                    print(related_data_qs[index])
                                    values += related_data_qs[index].related_sale, related_data_qs[index].date_selection, related_data_qs[index].toronto_booth_option, related_data_qs[index].toronto_additional_booth_option
                                except IndexError:
                                    values += ['-', '-', '-', '-']
                            return values
                        except AttributeError:
                            return ['Something Maybe?!?!']

                    elif key == 'calgary':
                        try:
                            obj = obj.calgary_booking
                            return obj, obj.calgary_dates, obj.calgary_booth_option_1, obj.calgary_booth_option_2, obj.calgary_booth_option_3,  obj.calgary_date_1, obj.calgary_date_2, obj.calgary_date_3, obj.calgary_additional_booth_option_1, obj.calgary_additional_booth_option_2, obj.calgary_additional_booth_option_3, obj.calgary_additional_lunch_option_1, obj.calgary_additional_lunch_option_2, obj.calgary_additional_lunch_option_3, obj.calgary_diet_request_1, obj.calgary_diet_request_2, obj.calgary_diet_request_3, obj.calgary_venue_options
                        except AttributeError:
                            return ['-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-', '-']
                    elif key == 'edmonton':
                        try:
                            obj = obj.edmonton_booking
                            return obj, obj.edmonton_dates, obj.edmonton_date_1, obj.edmonton_date_2, obj.edmonton_date_3, obj.edmonton_date_4, obj.edmonton_booth_option_1, obj.edmonton_booth_option_2, obj.edmonton_booth_option_3, obj.edmonton_booth_option_4, obj.edmonton_additional_booth_option_1, obj.edmonton_additional_booth_option_2, obj.edmonton_additional_booth_option_3, obj.edmonton_additional_booth_option_4, obj.edmonton_additional_lunch_option_1, obj.edmonton_additional_lunch_option_2, obj.edmonton_additional_lunch_option_3, obj.edmonton_additional_lunch_option_4, obj.edmonton_additional_breakfast_option_1, obj.edmonton_additional_breakfast_option_2,  obj.edmonton_additional_breakfast_option_3, obj. edmonton_additional_breakfast_option_4, obj.edmonton_diet_request_1, obj.edmonton_diet_request_2, obj.edmonton_diet_request_3, obj.edmonton_diet_request_4, obj.edmonton_venue_options
                        except AttributeError:
                            return ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
                    elif key == 'winnipeg':
                        try:
                            obj = obj.winnipeg_booking
                            return obj, obj.winnipeg_dates, obj.winnipeg_date_1, obj.winnipeg_date_2, obj.winnipeg_date_3, obj.winnipeg_booth_option_1, obj.winnipeg_booth_option_2, obj.winnipeg_booth_option_3, obj.winnipeg_additional_booth_option_1, obj.winnipeg_additional_booth_option_2, obj.winnipeg_additional_booth_option_3, obj.winnipeg_additional_lunch_option_1, obj.winnipeg_additional_lunch_option_2, obj.winnipeg_additional_lunch_option_3, obj.winnipeg_diet_request_1, obj.winnipeg_diet_request_2, obj.winnipeg_diet_request_3
                        except AttributeError:
                            return ['-', '-', '-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
                # except AttributeError:
                #     return None
            writer.writerow((
                smart_str(u"Order ID"),
                smart_str(u"Company Name"),
                smart_str(u"Contact Name"),
            ))

            for obj in queryset:
                print(get_attributes_of_forgien_key_obj(obj, 'toronto'))

                writer.writerow([
                    smart_str(obj.pk),
                    smart_str(obj.company_name),
                    smart_str(obj.contact_name)
                ])

            return response

        export_csv.short_description = u"Export All Data"

        actions = [export_csv]

# Register your models here.
admin.site.register(SalesFormData, MyModelAdmin.SalesAdmin)
