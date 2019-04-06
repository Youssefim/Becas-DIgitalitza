
a= float(input("Enter a number: "))
b=float(input("Enter another number: "))
suma=a+b
resta=a-b
div=a/b
mul=a*b

print("1. SUMA\n2. RESTA\n3. MUL\n4. DIV")
x=float(input("operacion que quieres: "))
if(x==1):
    print(suma)
elif(x==2):
    print(resta)
elif(x==3):
    print(mul)
elif(x==4):
    print(div)
else:
    print("ENTER A VALID OPTION ASSHOLE")