# def factorial(n):
#     if n==1:
#         return 1
#     else :
#      return n*factorial(n-1)
#
# print(factorial(6))



# x = int(input("Enter numbers of fibonacci series: "))
# n1, n2 = 0, 1
# sum1 = 0
# for i in range(x):
#     print(sum1, end=" ")
#     n1 = n2
#     n2 = sum1
#     sum1 = n1+n2

x = int(input("Enter numbers of fibonacci series: "))

arr = [0, 1]
for i in range(2,x):
    arr.append(arr[i-1] + arr[i-2])
print (arr)

