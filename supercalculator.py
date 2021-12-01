import math
import time

print("this is the super calculator.\n this contains: \n + \n - \n * \n / \n pytagorean theorem \n")
while True:
    operation = input("what operation? \n + \n - \n * \n / \n pytagorean theorem \n")
    if operation == '+':
        add1 = int(input("what is your first number?"))
        add2 = int(input("what is your second number?"))
        print("adding....")
        time.sleep(0.75)
        print(add1 + add2)
        endadd = input("end? [y/n]")
        if endadd == "y":
            break
    if operation == "-":
        sub1 = int(input("what is your first number?"))
        sub2 = int(input("what is your second number?"))
        print("subtracting....")
        time.sleep(0.75)
        print(sub1-sub2)
        endsub = input("end? [y/n]")
        if endsub == "y":
            break
    if operation == "*":
        mul1 = int(input("what is your first number?"))
        mul2 = int(input("what is your second number?"))
        print("multiplying....")
        time.sleep(0.75)
        print(mul1 * mul2)
        endsub = input("end? [y/n]")
        if endsub == "y":
            break
    if operation == "/":
        div1 = int(input("what is your first number?"))
        div2 = int(input("what is your second number?"))
        print("dividing....")
        time.sleep(0.75)
        print(div1/div2)
        enddiv = input("end? [y/n]")
        if enddiv == "y":
            break
    if operation == "pytagorean theorem":
        leg1 = int(input("what is your first leg?"))
        leg2 = int(input("what is your second leg?"))
        print("calculating....")
        time.sleep(0.75)
        sqrresult = (leg1*leg1+leg2*leg2)
        print(math.sqrt(sqrresult))
        end = input("end? [y/n]")
        if end == "y":
            break
    
        
