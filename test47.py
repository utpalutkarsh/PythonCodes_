# def fibonacci(n):
#     if n ==0 or n ==1:
#        return n
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)
#
# for i in range(5):
#     print(fibonacci(i), end = ' ')

def fibonacci(n):
    fib_list= [0,1]
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])

    return fib_list



# def fibonacci(n):
#     temp = 0
#     current = 1
#     sum = 0
#     for i in range(n):
#         print(sum, end=' ')
#         temp = current
#         current = sum
#         sum = temp +current


print(fibonacci(6))