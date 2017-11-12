class MainCalc():

    res = 0

    def __init__(self, num1):
        self.num1 = num1
        self.num2 = 15
    
    def sum(self):
        res = self.num1 + self.num2
        return res
    def subs(self):
        res = self.num1 - self.num2
        return res
    def mult(self):
        res = self.num1 * self.num2
        return res
    def div(self):
        res = self.num1 / self.num2
        return res


res = 0
while True:
    option = int(input("Hi\nThis is a simple calculator\nPress for following options\n1 for sum\n2 for substract\n3 for multiplication\n4 for division\nEnter here: "))
    num1 = int(input("Add a number: "))
    calc = MainCalc(num1)
    
    if option == 1:
        res = calc.sum()
    elif option == 2:
        res = calc.subs()
    elif option == 3:
        res = calc.mult()
    elif option == 4:
        res = calc.div()
    else:
        print("Add a number from the menu!!")
        break
print("The result of selected operation is: ", res)

    
    
