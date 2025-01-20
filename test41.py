x = int(input("Enter the number of elements of fibonacci series: "))
y = 0
z = 1
sum1 = 0
for i in range(x):
    print(sum1, end=" ")
    y = z
    z = sum1
    sum1 = y+z