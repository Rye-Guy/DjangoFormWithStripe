def calculate_fair_total(obj):
    from .models import TorontoFair, EdmontonFair, CalgaryFair, WinnipegFair
    # .5 tax bracket #
    low_tax_provinces = ['Alberta', 'British Columbia', 'Manitoba', 'Quebec', 'Saskatchewan', 'Northwest Territories',
                         'Nunavut', 'Yukon']
    # .13 tax bracket #
    ont_tax_text_value = 'Ontario'

    # .15 tax bracket #
    high_tax_provinces = ['New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Prince Edward Island']

    someTotal = 0

    if obj.related_class() != 'toronto':
        lunch_cost = int(obj.additional_lunch_option) * 28
        someTotal += lunch_cost
        if obj.related_class() != 'winnipeg':
            if obj.wifi == True:
                someTotal += 50
            if obj.electricity == True:
                someTotal += 129
        if obj.related_class == 'edmonton':
            breakfast_cost = int(obj.additional_breakfast_option) * 25
            someTotal += breakfast_cost

    province = obj.related_sale.province
    booth_option = obj.booth_option
    additional_booth_option = int(obj.additional_booth_option) * 995
    tax_cal = obj.related_sale.province
    discount = obj.related_sale.discount_percentage
    discount_dec = discount.replace('%', '.')
    someTotal += int(booth_option) + additional_booth_option
    purchase_discount = int(someTotal) * float(discount_dec)
    my_cost_bf_tax = someTotal - purchase_discount


    if province in low_tax_provinces:
        tax_to_charge = 0.05
        tax_to_charge = my_cost_bf_tax * tax_to_charge
        my_cost_af_tax = my_cost_bf_tax + tax_to_charge
    elif province == ont_tax_text_value:
        tax_to_charge = 0.13
        tax_to_charge = my_cost_bf_tax * tax_to_charge
        my_cost_af_tax = my_cost_bf_tax + tax_to_charge
    elif province in high_tax_provinces:
        tax_to_charge = 0.15
        tax_to_charge = my_cost_bf_tax * tax_to_charge
        my_cost_af_tax = my_cost_bf_tax + tax_to_charge

    obj.subtotal = someTotal
    obj.discount_cost = purchase_discount
    obj.grand_total = my_cost_af_tax
    obj.tax_to_charge = tax_to_charge



    print(someTotal, tax_cal, discount_dec, my_cost_bf_tax, tax_to_charge, my_cost_af_tax)

    if obj.related_class() == 'toronto':
        TorontoFair.objects.all().filter(id=obj.id).update(subtotal=someTotal, discount_cost=purchase_discount, tax_to_charge=tax_to_charge, grand_total=my_cost_af_tax)
    elif obj.related_class() == 'calgary':
        CalgaryFair.objects.all().filter(id=obj.id).update(subtotal=someTotal, discount_cost=purchase_discount, tax_to_charge=tax_to_charge, grand_total=my_cost_af_tax)
    elif obj.related_class() == 'edmonton':
        EdmontonFair.objects.all().filter(id=obj.id).update(subtotal=someTotal, discount_cost=purchase_discount, tax_to_charge=tax_to_charge, grand_total=my_cost_af_tax)
    elif obj.related_class() == 'winnipeg':
        WinnipegFair.objects.all().filter(id=obj.id).update(subtotal=someTotal, discount_cost=purchase_discount, tax_to_charge=tax_to_charge, grand_total=my_cost_af_tax)


