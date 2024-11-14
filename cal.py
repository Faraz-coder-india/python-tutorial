print('''
      + ADD
      - SUBTRACT
      * MULTIPLY
      / DIVIE
      ''')
num1=int(input("Enter the value1:-"))
num2=int(input("Enter the value2:-"))
opr=input("Enter The Opr..(=,-,*,+)")

if opr=="+":
    print(num1+ num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    Print("incalid Opr....")

