import market_products_list_001 as products

class purchase():

    def __init__(self) :
        self.list_of_products = [{ 'id' : '9999999','name' : 'test','price_kg' : 9999999,'qty' : 9999999,}] ## variables of the class usingn self private word to acess,every function can acess those variables, had to start using a random variable to compare,otherwise it wouldnt compare the variables and wouldnt run the code
        pass
        
        
    def items_to_buy(self,products):
        inside_list = False
        item_counter = 0;

        for  i in self.list_of_products :
            if i['id'] == products['id'] :
                inside_list = True
                i['qty'] = i['qty']+1

            if i['id'] != products['id'] :
                inside_list = False
                item_counter = item_counter +1
                pass
        
        if item_counter == len(self.list_of_products) :
            self.list_of_products.append(products)

        if len(self.list_of_products) > 1 and self.list_of_products[0]['id'] == '9999999' :
            self.list_of_products.pop(0)

        return self.list_of_products

    def show_items(self) :

        for i in self.list_of_products :
            print( 'id : ', i['id'],'//', 'name : ', i['name'], '//', 'price : ', i['price'], '//', 'quantity : ', i['qty'] )

    def items_properties(self,item) :

        print('index of item is : ',self.list_of_products.index(item))
        index_of_item = self.list_of_products.index(item)
        property_of_item = self.list_of_products[index_of_item]

        return property_of_item

    def total_to_pay(self) :

        total_amount = 0;

        for  i in self.list_of_products :
            total_price_item = i['qty']*i['price']
            total_amount = total_amount + total_price_item
        
        print('the total to pay is : ',total_amount)
        return total_amount





item1 = products.chicken_meat_02
item2 = products.bread_01
item3 = products.juice_bottle01

comprador1 = purchase()

comprador1.items_to_buy(item1)
comprador1.items_to_buy(item2)
comprador1.items_to_buy(item3)
comprador1.items_to_buy(item1)

print(comprador1.list_of_products)
##print(comprador1.list_of_products[2])
##print(comprador1.list_of_products[0])

for item in comprador1.list_of_products :
    print(item['qty'])

comprador1.show_items()

comprador1.items_properties(item1)

bread = comprador1.items_properties(item2)
bread['price'] = 10
bread['qty'] = 1

comprador1.show_items()



##comprador1.items_to_buy(products.chocolate_bar01)
##comprador1.items_to_buy(products.juice_bottle01)



##for name in vars(products): ## get all the variables from a script, returns the dictonary attribute of an object, the elements inside a script can be used as parameters as well
##    print(name)

##for name in vars(products).values() :
##    print(name)

##for name,value in vars(products).items() :
##    print(name,value)

##x = products.bread_01
##print(x['id'])

##import data
##for name ,values in vars(data).items():
##    print(name, values)