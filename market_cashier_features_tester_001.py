import market_cashier_functions_001 as mcf
import market_products_list_001 as mp

## functions of the code and its parameters :
## items_to_buy(products)
## show_items()
## items_properties(item)
## total_to_pay()

item1 = mp.juice_bottle01
item2 = mp.meat_01
item3 = mp.rice_02

buyer1 = mcf.purchase()

buyer1.items_to_buy(item1)
buyer1.items_to_buy(item2)
buyer1.items_to_buy(item3)

good1 = buyer1.items_properties(item1)
good2 = buyer1.items_properties(item2)
good3 = buyer1.items_properties(item3)

good1['price'] = 5.00
good2['price'] = 27.50
good3['price'] = 6.00

good1['qty'] = 1
good2['qty'] = 0.500
good3['qty'] = 1.000

buyer1.show_items()

buyer1.items_to_buy(item1)

buyer1.show_items()

buyer1.total_to_pay()


""" dic1 = {
    'id' : 'test',
    'var' : 1
}

dic2 = {
    'id' : 999,
    'var' : 1
}

if dic1 == dic2 :
    print('equal')
else :
    print('different')

if dic1['id'] == dic2['id'] :
    print('equal')
else :
    print('different')

array_test = [dic1,dic2]

print(array_test.index(dic1)) """