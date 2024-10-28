class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

#for nomodification
class nomod(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def choose_final(self):
        deal = input("Enter 'yes' if this is your final choice and 'no' if you want to change: ")
        deal = deal.lower()
        if deal == "yes":
            self.final()
        elif deal == "no":
            pass

    def final(self):
        print(f"Your final car is ready.\nName={self.brand} \nModel={self.model} \nTyres=default  \nExhaust=default")
        
    

#for modification
class modification(Car):
    def __init__(self, brand, model, tyre, exhaust):
        super().__init__(brand, model)
        self.tyre = tyre
        self.exhaust = exhaust

    def final(self):
        print(f"Your final car is ready.\nName={self.brand} \nModel={self.model} \nTyres={self.tyre} \nExhaust={self.exhaust}")

    def choose_final(self):
        deal = input("Enter 'yes' if this is your final choice and 'no' if you want to change: ")
        deal = deal.lower()
        if deal == "yes":
            self.final()
        elif deal == "no":
            pass


def modchange():
    chg_in = input("Enter what would you like to change (brand, model, tyre, exhaust): ")
    chg_in = chg_in.lower()
    if chg_in == "brand":
        b = input("Enter car's brand: ")
        m = input("Enter car's model: ")
        mo = modification(b, m, ty, exh)
        mo.choose_final()
    elif chg_in == "model":
        m = input("Enter car's model: ")
        mo = modification(b, m, ty, exh)
        mo.choose_final()
    elif chg_in == "tyre":
        ty = input("Enter tyres you want: ")
        mo = modification(b, m, ty, exh)
        mo.choose_final()
    elif chg_in == "exhaust":
        exh = input("Enter exhaust you want: ")
        mo = modification(b, m, ty, exh)
        mo.choose_final()


def nomodchange():
    chg_in = input("Enter what would you like to change (brand, model): ")
    chg_in = chg_in.lower()
    if chg_in == "brand":
        b = input("Enter car's brand: ")
        nomo = nomod(b, m)
        nomo.choose_final()
    elif chg_in == "model":
        m = input("Enter car's model: ")
        nomo = nomod(b, m)
        nomo.choose_final()


b = input("Enter car's brand: ")
m = input("Enter car's model: ")
mod = input("Enter 'yes' if you want modification and 'no' if you do not want modification: ")
if mod.lower() == "yes":
    ty = input("Enter tyres you want: ")
    exh = input("Enter exhaust you want: ")
    mo = modification(b, m, ty, exh)
    mo.choose_final()
elif mod.lower() == "no":
    nomo = nomod(b, m)
    nomo.choose_final()
