# n=10
# for i in range(1,n+1):
#     print(i,end=" ")
# print()

# n=10
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i,end=" ")
# print() 

# n=10
# for i in range(1,n+1):
#     if i % 2 != 0:
#         print(i,end=" ")
# print()

# n=10
# for i in range(2,n+1):
#     if i % 2 == 0:
#         print(i,":", "even")
#     else:
#         print(i,":", "odd")
# print()

# n=20
# even_list=[]
# odd_list=[]
# even_count=0
# odd_count=0
# for i in range(2,n+1):
#     if i % 2 == 0:
#         even_list.append(i)
#         even_count+=1
#     else:
#         odd_list.append(i)
#         odd_count+=1
# print("Even numbers:", even_list)
# print("Even count:", even_count)
# print("Odd numbers:", odd_list)
# print("Odd count:", odd_count)


# x=int(input("Enter a number: "))
# n = 10
# for i in range(1,n+1):
#     print(x,"*",i,"=",x*i)
# print()

# n=100
# for i in reversed(range(10,n+1,10)):
#     print(i,end=" ") 
# print()

# n = 51
# if n <= 1:
#     print("No prime numbers in the given range.")
# else:
#     for i in range(2,n+1):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i,end=" ")
# print() 

# n=int(input("Enter a number: "))
# if n <= 1:
#     print("No prime numbers in the given range.")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print(n,"is not a prime number.")
#             break
            
#     else:
#         print(n,"is a prime number.")


# n=5
# factorial=1
# for i in range(1,n+1):
#     factorial *= i
# print("Factorial of", n, "is", factorial)


# a,b=10,20
# for i in range(1,6):
#     a+=i
#     b-=i  
# print("a =", a)
# print("b =", b)

# n= 10   
# a,b = 0,1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b = b, a + b
# print()

# a,b = 24,36
# x, y = a, b
# while y:
#     x, y = y, x % y
# gcd = x
# lcm = (a * b) // gcd

# print("GCD of", a, "and", b, "is", gcd)
# print("LCM of", a, "and", b, "is", lcm)

# x= 12345
# temp = x
# reverse=0
# while x > 0:
#     digit = x % 10
#     reverse = reverse * 10 + digit
#     x //= 10
# print("Reversed number:", reverse)

# if temp == reverse:
#     print(temp, "is a palindrome.")
# else:   
#     print(temp, "is not a palindrome.")


# x= 12345
# sum_of_digits=0
# while x > 0:
#     digit = x % 10
#     sum_of_digits += digit
#     x //= 10
# print("Sum of digits:", sum_of_digits)
# x= 12345
# product_of_digits=1
# while x > 0:
#     digit = x % 10
#     product_of_digits *= digit
#     x //= 10

# print("Product of digits:", product_of_digits)

# x= 23456
# count_even=0
# count_odd=0
# sum_even=0
# sum_odd=0
# while x > 0:
#     digit = x % 10
#     if digit % 2 == 0:
#         count_even += 1
#         sum_even += digit
#     else:
#         count_odd += 1
#         sum_odd += digit
#     x //= 10
# print("Count of even digits:", count_even) 
# print("Count of odd digits:", count_odd)
# print("Sum of even digits:", sum_even)
# print("Sum of odd digits:", sum_odd)

# x= 12345
# largest_digit=0
# while x > 0:
#     digit = x % 10
#     if digit > largest_digit:
#         largest_digit = digit
#     x //= 10
# print("Largest digit:", largest_digit)

# x= 12345
# smallest_digit=9
# while x > 0:
#     digit = x % 10
#     if digit < smallest_digit:
#         smallest_digit = digit
#     x //= 10
# print("Smallest digit:", smallest_digit)

# x = 153
# temp = x
# sum_of_cubes = 0 
# while x > 0:
#     digit = x % 10
#     sum_of_cubes += digit ** 3
#     x //= 10
# if sum_of_cubes == temp:
#     print(temp, "is an Armstrong number.")
# else:
#     print(temp, "is not an Armstrong number.")  

# x = 1234
# temp = x
# sum_of_squares = 0
# while x > 0:    
#     digit = x % 10
#     sum_of_squares += digit ** 2
#     x //= 10
# print("Sum of squares of digits:", sum_of_squares)


# n=11
# total=0 
# result = []
# for i in range(1,n+1):
#      total += i**2
#      result.append(total)
# print(total)
# print(result)

# n=11
# total=0 
# result = {}
# for i in range(1,n+1):
#      total += i**2
#      result[i] = i **2 
# print(total)
# print(result)