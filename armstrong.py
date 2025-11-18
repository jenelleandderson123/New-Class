num = int(input("Enter a number please"))
sum = 0

# finding the sum of the cube for each digit

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "Is an armstrong number")
else:
    print("The number is not an armstrong number")