from django.contrib import admin
from .models import TorontoFair, CalgaryFair, EdmontonFair, WinnipegFair
# Register your models here.
import import_export


class FairModelResource(import_export.resources.ModelResource):

    class Meta:
        model = TorontoFair


class FairAdmin(import_export.admin.ImportExportModelAdmin):
    list_display = ['id', 'get_related_data','related_sale']
    #list_display += ('toronto_booking_id', 'get_related_bookings_toronto')
    search_fields = ['related_sale__id']
    resource_class = FairModelResource

    def get_related_data(self, obj):
        try:
            return obj.related_sale.company_name

        except AttributeError:
            return obj.related_sale
    get_related_data.short_description = 'Company Name'





admin.site.register(TorontoFair, FairAdmin)
admin.site.register(CalgaryFair, FairAdmin)
admin.site.register(EdmontonFair, FairAdmin)
admin.site.register(WinnipegFair, FairAdmin)