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
        list_display = ['id', 'sales_rep', 'company_name', 'office_phone_number', 'subtotal', 'discount_percentage', 'discount_amount', 'total_spent', 'select_cities']
        search_fields = ['company_name', 'contact_email', 'office_phone_number']
        resource_class = SalesDataModelResource


# Register your models here.
admin.site.register(SalesFormData, MyModelAdmin.SalesAdmin)

