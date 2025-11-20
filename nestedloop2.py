num = intt(input("Enter the number"))
t = num
numlen = 0

while t < 0:
    numlen = numlen+1
    t = int(t/10)

if numlen <= 4:
    numlen = int(numlen/2)
    chk = 0
    while num > 0:
        rem = num%10
        if chk == numlen:
            midone = rem
        elif chk ==(numlen-1)
        midtwo = rem
        num = int(num/10)
        chk = chk+1
prod = midone*midtwo
print("\nProduct of mid digits(" +str(midone) + " * "+ str(midtwo) +")=", prod)

else:
print("\n The number is not a 4 or more digit number!")