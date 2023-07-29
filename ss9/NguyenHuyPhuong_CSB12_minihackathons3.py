#phần 1
# def checking_num(num):
#     if num % 2 ==0:
#         return True
#     else: False
# num=int(input("Input a number: "))
# result = checking_num(num)
# if result:
#     print("this number is even")
# else:
#     print("this number is not even")


# import math
# def cal_area(radius):
#     area = math.pi * (radius**2)
#     return area
# radius = float(input("Input radius: "))
# area = cal_area(radius)
# print("Circle’s area:",area)


# def reverse_str(string):
#     return string[::-1]
# input = input("Input a text: ")
# reversed_str = reverse_str(input)
# print ("Reversed text: ", reversed_str)


# def is_palindrome(string):
#     reverse_string = string[::-1]
#     if string == reverse_string:
#         return True
#     else:
#         return False
# input_text = input("Input a text: ")
# if is_palindrome(input_text):
#     print("this is a palindrome")
# else:
#     print("this is not a palindrome")


# def meth(n):
#     if n ==0:
#         return 1
#     else:
#         return n*meth(n-1)
# n=int(input("Input a number: "))
# result = meth(n)
# print (f"{n}!: {result}")

# list1=[5, 1, 8, 92, -1, 30]
# print("og list:", list1)
# def sort_list(list):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i] > list[j]:
#                 list[i], list[j]=list[j], list[i]
#     return list
# list2= sort_list(list1)
# print("sorted list: ", list2)


# def print_fibo(n):
#     if n<= 0:
#         print("Number is must larger than 0")
#     elif n==1:
#         print ("1")
#     elif n==2:
#         print("1 1")
#     else:
#         fibo =[1,1]
#         for i in range(2, n):
#             fibo.append(fibo[i-1] + fibo[i-2])
#             print(' '.join(str(x) for x in fibo))
# n = int(input(" Input a number: "))
# print (f"First {n} Fibonacci number: ")
# print_fibo(n)
