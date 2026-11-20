# Separate even and odd numbers

numbers = [2,4,5,6,7,8,9,99,11,28,90]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else: 
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)