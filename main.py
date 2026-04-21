class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases


    

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)


    # def add_purchase(self, name, purchase):
    #     if purchase is list:
    #         self.add_customer(name, [purchase])
    #     else:
    #         self.add_customer(name, purchase)



    def generate_report(self):
        for y, x in self.customers.items():
            a = 0
            for z in x:
                a += self.__add_tax(z['price'])

            print(y)



            if a > self.discount_threshold:
                print("Eligible for discount")
            elif a > 300:
                print("Potential future discount customer")
            else:
                print("No discount")

            if a > 1000:
                print("VIP Customer!")
            else:
                if a > 800:
                    print("Priority Customer")


    def __add_tax(self, amount):
        if amount > self.tax_threshold:
            return amount * (1 + self.tax_rate)
        else:
            return amount





    def calculate_shipping_fee(self, purchases):
        heavy_item = False
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                heavy_item = True
                break
        if heavy_item:
            return 50
        else:
            return 20

def calculate_shipping_fee_for_heavy_items(purchases):
    for purchase in purchases:
        if purchase.get('weight', 0) > 20:
            return 50
    return 20

def calculate_shipping_fee_for_fragile_items(purchases):
    fragile_item = False
    for purchase in purchases:
        if purchase.get('fragile', False):
            fragile_item = True
            break
    if fragile_item:
        return 60
    else:
        return 25

flat_tax = 0.2