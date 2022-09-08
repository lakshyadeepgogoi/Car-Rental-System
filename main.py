class carShop:

    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total cars", self.stock)

    def rentForBike(self, q):
        if q <= 0:
            print("Enter the positive value or greater than zero")
        elif q > self.stock:
            print("enter the value  less than stock")

        else:
            self.stock = self.stock - q
            print("Total prices", q * 100)
            print("Total car", self.stock)


while True:
    obj = carShop(100)
    uc = int(input('''
  1 Display stocks
  2 Rent a Car
  3 Exit 
  '''))

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter the quantity----->"))
        obj.rentForBike(n)

    else:
        break
