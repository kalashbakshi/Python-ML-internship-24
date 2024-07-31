# Make a calculator...input as string
str=input("Enter your epression:")
op=""
for i in str:
    if i in "+-*/":
        op=i 
L=str.split(op)
if op=='+':
    print(float(L[0])+float(L[1]))
elif op=='-':
    print(float(L[0])-float(L[1]))
elif op=='*':
    print(float(L[0])*float(L[1]))
elif op=='/':
    print(float(L[0])/float(L[1]))
else:
    print("Invalid operator")