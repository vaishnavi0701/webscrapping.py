
# x=int(input("enter num :  "))
# z=x%10
# print(z)
# if z%3==0:
#     print("div by 3")
# else:
#     print("not")

# a=int(input("enter num : "))
# b=int(input("enter num : "))
# c=int(input("enter num : "))
# if a>b:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)
# 

# a=int(input("enter no"))
# num=a%10
# print(num)
# if num==3:
#     print("yes")
# else:
#     print("no")


# a=int(input("enter num"))


# num=int(input("enter num : "))
# a=(num//10)%10

# if a==2:
#     print(a,"yes")
# else:
#     print(a,"no")



# num=int(input("enter your number: "))
# i=1
# while i<=num:
#     j=1
#     while j<num:
#         j+=1
#     print( '"' +"q",str(i), '"','"' +"z",str(i),'"')     
#     print()
#     i+=1



# n=int(input("Enter the number: "))
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)



# for i in "string":
#     if i=="i":
#         break
#     print(i)


# for i in "string":
#     if i=="i":
#         continue
#     print(i)


# user1=int(input("number: "))
# user2=int(input("number: "))
# user3=int(input("number: "))
# if user1>user2:
#     print(user1,"greater")
# elif user2>user3:
#     print(user2,"greater")
# else:
#     print(user3,"graeter")

# a=int(input("enter angles : "))
# b=int(input("enter angles : "))
# c=int(input("enter angles : "))
# if a+b+c==180:
#     print("valid triangle")
# else:
#     print("not valid")


# a="python"
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[j],end=" ")
#         j=j+1
#     print()
# #     i=i+1

# Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F


# phy=int(input("enter num : "))
# chem=int(input("enter num : "))
# boi=int(input("enter num : "))
# math=int(input("enter num : "))
# com=int(input("enter num : "))
# a=(phy+chem+boi+math+com)/500*100
# print(a)
# if a>=90:
#     print(a,"grade A")
# elif a>=80:
#     print(a,"grade B")
# elif a>=70:
#     print("grade C")
# elif a>=60:
#     print(a,"grade D")
# elif a>=40:
#     print(a,"grade E")
# elif a<40:
#     print(a,"grade F")
# else:
#     print(a,"nothing")


# a=int(input("enter salary : "))
# if a<=10000:
#     print("HRA = 20%, DA = 80%")
# elif a<=20000:
#     print("HRA = 25%, DA = 90%")
# elif a>20000:
#     print("HRA = 30%, DA = 95%")


# Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit



# 1. Write a program to print the following using while loop 
# Puja Na. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers

# i=1
# while i<=20:
#     if i%2==0:
#         print(i,"even")
#     i=i+1

# i=1
# while i<=20:
#     if i%2!=0:
#         print(i,"odd")
#     i=i+1


# i=1
# while i<=10:
#     print(i)
#     i=i+1


# i=0
# while i<=9:
#     print(i)
#     i=i+1

# 2. Write a program to print first 10 integers and their squares like
# 1 1
# 2 4
# 3 9 
# ………………...and so on

# i=1
# while i<=10:
#     print(i,i*i)
#     i=i+1

# 3. Write while loop  statement to print the following series:
# 10, 20, 30 … … 300

# i=10
# while i<=300:
#     print(i,end=" ")
#     i=i+10

# 4. Write a while loop  statement to print the following series
# 105, 98, 91 ………7

# i=105
# while i>=7:
#     print(i)
#     i=i-7

# 5. Write a program to print the first 10 natural numbers in reverse order.

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# 6. Write a program to print the sum of the first 10 Natural numbers.

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

# 7. Write a program to print the sum of the first 10 Even numbers.

# i=1
# sum=0
# while i<=20:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print(sum)

# 8. Write a program to print a table of a number entered from the user.
# a=int(input("enter num : "))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i=i+1

# a=input("enter alphabet : ")
# if a>="a" and a<="z":
#     print("lower")
# elif a>="A" and a<="Z":
#     print("upper")
# else:
#     print("wrong input")


# 9. Write a program to display all even numbers that fall between two numbers (exclusive both numbers) entered by the user.

# a=int(input("enter num : "))
# b=int(input("enter num : "))
# i=1
# while a<=b:
#     if i%2==0:
#         print(i)
#     i=i+1

# # 10. Write a program to check whether a number is prime or not.

# num=int(input("enter num : "))
# i=0
# a=1
# while i<=num:
#     if num%a==0:
#         a=a+1
#     i=i+1
# if a==2:
#     print("prime")
# else:
#     print("not")

# 11. Write a program to find the sum of the digits of a number accepted from the user.

# n=int(input("Enter a number:"))
# sum=0
# while(n>0):
#     a=n%10
#     sum=sum+a
#     n=n//10
# print(sum)

# 13. Write a program to reverse the number accepted by the user.

# n=int(input("enter number"))
# i=0
# while n>0:
#     i=(i*10)+n%10
#     n=n//10
# print(i)
# i=i+1
    
# 14. Write a program to display the number names of the digits of if the number is 231 then output should be Two a number entered by user, for example Three One


















# 15. Write a program to print the Fibonacci series till n terms (Accept n from user)

# num=int(input("enter num : "))
# a,b=0,1
# i=0
# while i<num:
#     if i==0:
#         print(0)
#     print(b)
#     a,b=b,a+b
#     i=i+1

# 16. Write a program to print the factorial of a number accepted by the user.

# a=int(input("enter num : "))
# i=1
# b=1
# while i<=a:
#     b=b*i
#     i=i+1
# print(b)




# 17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)

# num=int(input("enter num : "))
# n=num
# i=1
# sum=0
# while i<=n:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if num==sum:
#     print(sum,"amt")
# else:
#     print(sum,"not")

# num=int(input("enter the number"))
# n=num
# i=1
# sum=0
# while i<=n:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if num==sum:
#     print(sum,"amt")
# else:
#     print(sum,"not")

# 20. Write a program to check whether a number is palindrome or not.

 
# n=int(input("Enter number:"))
# a=n
# b=0
# while(n>0):
#     d=n%10
#     b=b*10+d
#     n=n//10
# if(a==b):
#     print("palindrome")
# else:
#     print("not palindrome")

# n=int(input("enter the number:"))
# a=n
# b=0
# while (n>0):
#     d=n%10 
#     b=b%10+d 
#     n=n//10
# if (a==b):
#     print("palindrome")




# 22. Write a program to accept 10 numbers from the user and display it’s average.

# i=1
# sum=0
# avg=1
# while i<=10:
#     a=int(input("enter num : "))
#     sum=sum+a
#     avg=sum/10
#     i=i+1
# print(avg)





# 23. Write a program to accept 10 numbers from the user and display the largest & smallest number.













# 24. Write a program to display sum of odd numbers and even numbers separately that fall between two numbers accepted from the user.(including both numbers) 100 and 500

# i=100
# a=0
# b=0
# while i<=500:
#     if i%2==0:
#         a=a+i
#     else:
#         b=b+i
#     i=i+1
# print(a)
# print(b)

# 26. Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms














# 27. Write a program to print the following series till n terms.1 4 9 16 25 _ _ _ _ _ n  terms

# n=int(input("enter num : "))
# i=1
# while i<=n:
#     print(i*i,end=" ")
#     i=i+1

# 31. Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms

# i=1
# while i<=120:
#     print(i*i+i,end=" ")
#     i=i+1


# 33. Write a Program to print all the characters in the string ‘COMPUTER’ using a while loop .

# a="computer"
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1
# # print(i)




# 35. Write a program to print all the factors of a number using a while loop .


# a=int(input("enter num : "))
# i=1
# b=1
# while i<=a:
#     b=b*i
#     i=i+1
#     print(b)

# 36. Accept two numbers from the user and display sum of even numbers between them(including both)

# a=int(input("enter num : "))
# b=int(input("enter num : "))
# i=1
# c=0
# while i<=b:
#     if i%2==0:
#         c=c+i
    
#     i=i+1
#     print(i)
# # print(c)

# a=int(input("enter num : "))
# b=int(input("enter num : "))
# c=int(input("enter num : "))
# if a>b and a>c and b>c:
#     print(b ,"second greatest")
# elif b>a and b>c and a>c:
#     print(a ,"second greatest")
# elif c>b and c>a and b>a:
#     print(b ,"second greatest")
# if a>b and a>c and c>b:
#     print(c ,"second greatest")
# elif b>a and b>c and c>a:
#     print(c ,"second greatest")
# elif c>b and c>a and a>b:
#     print(a ,"second greatest"

#     # The original list is: 

# a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# b=""
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b+=a[i][j]
#             j+=1
#     i+=1
# print(b)


# List product excluding duplicates.
#     List = [6,1,3,5,6,3,1]
#     Output: 60

# list = [6,1,3,5,6,3,1]
# i=0
# while i<len(list):
#     j=i+1
#     while j<len(list):
#         if list[i]==list[j]:
#             del(list[j])
#         j=j+1
#     i=i+1
# print(list)
# k=0
# pro=1
# while k<len(list):
#     pro=pro*list[k]
#     k=k+1
# print(pro)


# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.

# a= [1, 2, 2, 5, 8, 4, 4, 8]
# i=0
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         if a[i]==a[j]:
#             del(a[j])
#         j=j+1
#     i=i+1
# print(a)
# print(i)

# Find the First Maximum, Second maximum, Third maximum number from the List.


# number=[1, 8, 3, 4, 9, 6, 7]
# max=number[0]
# i=0
# while i<len(number):
#     if number[i]>max:
#         max=number[i]
#     i=i+1
# print(max)
# max2=number[0]
# i=0
# while i<len(number):
#     if number[i]!=max:
#         max2=number[i]
#     i=i+1
# print(max2)


# a=[1, 8, 3, 4, 9, 6, 7]
# i=0
# max=0
# while i<len(a):


# For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.

# num=input("Enter a number")
# final=""
# i=0
# while i<len(num):
#     final+=str(int(num[i])**2)
#     i=i+1
# print(final)

# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'


# # Remove duplicates from a list.
# # List = [1,2,3,1,2,2]
# # Output: [1,2,3]
# a= [1,2,3,1,2,2]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print(b)



# a= [1,2,3,1,2,2]
# i=0
# b=[]
# while i<len(a):
#     if a.count(a[i])>1 and a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print(b)



# Remove empty List from List        
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

# a=[5, 6, [], 3, [], [], 9]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b)
            

# # list1 = [2, -7, 5, -64, -14]
# # Output: pos = 2, neg = 3

# a= [2, -7, 5, -64, -14]
# i=0
# b=[]
# c=[]
# d=0
# e=0
# while i<len(a):
#     if a[i]>0:
#         b.append(a[i])
#         d=d+1
#     else:
#         c.append(a[i])
#         e=e+1
#     i=i+1
# print(b,"count : ",d)

# print(c,"count : ",e)


# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7

# a=[12, 67, 98, 34]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     temp=str(a[i])
#     while j<len(temp):
#         sum+=int(temp[j])
#         j+=1
#     b.append(sum)
#     i+=1
# print(b)

# The original list is : [15, 81, 11, 234]
# List Integer Summation : [6,9,2,9]

# a=[15, 81, 11, 234]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     c=str(a[i])
#     while j<len(c):
#         sum=sum+int(c[j])
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)

# # Write a Python program to remove all the values except integer values from a given array of mixed values. 
# a=[34.67, 12, -94.89, 'Python', 0, 'C#']
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==int:
#         c.append(a[i])
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)
# print(c)

# # Write a Python program to check if first digit/character of each element in a given list is same or not.
# # Original list:
# # a=[1234, 122, 1984, 19372, 100]
# # Check if first digit in each element of the said given list is same or not!
# # True
# a=[1234, 122, 1984, 19372, 100]
# i=0
# while i<len(a):
#     temp=str(a[i])
#     if temp[0]=="1":
#         print(True)
#     else:
#         print(False)
#     i=i+1


# a=[1234, 922, 1984, 19372, 100]
# i=0
# while i<len(a):
#     b=str(a[i])
#     if b[0]=="1":
#         print(True)
#     else:
#         print(False)
#     i=i+1


# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']

# a=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i]+a[i+1])
#     i+=2
# print(b)

# Write a Python program to pair up the consecutive elements of a given list.
# Original lists:
# [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# 

# a= [1, 2, 3, 4, 5, 6]
# i=0
# b=[]
# while i<len(a):
#     b.append([a[i],a[i+1]])
#     i=i+1
# print(b)


# [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5]]


# a= [1, 2, 3, 4, 5,6]
# i=0
# b=[]
# while i<len(a):
#     b.append([a[i],a[i+1]])
#     i=i+2
# print(b)


# Write a Python program to check if a given string contains an element, which is present in a list. 
# The original string and list:
# https://www.w3resource.com/python-exercises/list/
# ['.com', '.edu', '.tv']
# Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
# True

# a="https://www.w3resource.com/python-exercises/list/"
# b=['.com', '.edu', '.tv']
# i=0
# while i<len(b):
#     if b[i] in a:
#         print(True)
#     else:
#         print(False)
#     i=i+1

# The original string and list: https://www.w3resource.net
# https://www.w3resource.net
# ['.com', '.edu', '.tv']
# Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
# False 


# a="https://www.w3resource.net"
# b=['.com', '.edu', '.tv']
# i=0
# while i<len(b):
#     if b[i] in a:
#         print(True)
#     else:
#         print(False)
#     i=i+1


#  Write a Python program to insert a specified element in a given list after every nth element.
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]


# a= [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# b=[]
# i=0
# count=0
# while i<len(a):
#     if count==4:
#         count=0
#         b.append("20")
#     b.append(a[i])
#     count+=1
#     i+=1
# print(b)
    
# Original list:
# ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# Insert Z in said list after every 3 th element:
# ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']

# a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# b=[]
# i=0
# count=0
# while i<len(a):
#     if count==4:
#         count=0
#         b.append("Z")
#     b.append(a[i])
#     count=count+1
#     i=i+1
# print(b)

# Write a Python program to add a number to each element in a given list of numbers.
# Original lists:
# [3, 8, 9, 4, 5, 0, 5, 0, 3]
# Add 3 to each element in the said list:
# [6, 11, 12, 7, 8, 3, 8, 3, 6]

# a=[3, 8, 9, 4, 5, 0, 5, 0, 3]
# i=0
# while i<len(a):
#     a[i]=a[i]+3
#     i=i+1
# print(a)

# Original lists:
# [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
# Add 0.51 to each element in the said list:
# [3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]

# a=[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0] 
# i=0
# while i<len(a):
#     a[i]=a[i]+0.51
#     i=i+1
# print(a)

#  Write a Python program to remove the last N number of elements from a given list. 
# Original lists:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# Remove the last 3 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# Remove the last 5 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
# Remove the last 1 element from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]

# a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]










# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}

# a={}
# for i,j in d1.items():
#     for x,y in d2.items():
#         if i==x:
#             a[i]=(j+y)
# # print(a)
# b={}
# for k in (d1,d2,b,a):
#     b.update(k)
# print(b)
        
# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


# a="w3resource"
# i=0
# b=0
# c={}
# for i in a:
#     if i not in c:
#         c[i]=1
#     else:
#         c[i]=c[i]+1
# print(c)



# Here's some python code that will do the trick. You will want to update VISITOR_PEOPLE. And if some people get to schedule before others, you'll need to reorder VISITOR_IDS.

# Edit: I added some more code to account for the fact that people can't be in a different place at the same time. You might want to make that more efficient (i.e. don't try to schedule a time that will not work). I'll let you figure that out though ;)

# num=int(input("enter num : "))
# sum=0
# i=0
# pro=1
# while i<=num:
#     rem=num%10
#     pro=pro//rem
#     num=num//10
#     pro==pro+1
# print(pro)

# a=int(input("enter njum :"))
# pro=1
# i=1
# while i<=a:
#     pro=pro*i
#     i=i+1
# print(pro)

# a=int(input("enter len :"))
# i=0
# prod=1
# while i<a:
#     p=int(input("enter num :"))
#     prod=p*prod
#     i=i+1
# print(prod)


# a=input("enter name : ")
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not")

# a="vaishnavi nalawade"
# print(a[12-1])

# a=["m","o","m"]
# b=[]
# i=1
# while i<=len(a):
#     b.append(a[-i])
#     i=i+1
# print(b)
# if a==b:
#     print("palindrome")
# else:
#     print("not")

# i=0
# while i<=10:
#     print(i*i,"",end="")
#     i=i+1

# num=int(input("enter the number"))
# if num<0:
#     print("number")
# else:
#     print(num*1)
#     print(num*2)
#     print(num*3)
#     print(num*4)
#     print(num*5)
#     print(num*6)
#     print(num*7)
#     print(num*8)
#     print(num*9)
#     print(num*10)

# user=int(input("enter the number"))
# a=(user//100)%10
# print(a)
# if a==3:
#     print("yes")
# else:
#     print("no")


# a=[1,2,3,4,5,6,7,8,9,10]
# c={}
# for i in a:
#     b={}
#     for j in range(0,i):
#         s=i*5
#         b.update({i:s})
#         # print(b)
#     c.update(b)
# print(c)


# def string(s):
#     upper=0
#     lower=0
#     for i in s:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#         else:
#             pass
#     print("original string",s)
#     print("no.of upper case char",upper)
#     print("no.of lower case char",lower)
# string("my name is VaishnaVi")

# n=int(input("Enter the number: "))
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

# count=0
# while count<3:
#     print("inside loop")
#     count+=1
# else:
#     print("outside loop")

# i=0
# while i<=5:
#     if i==3:
#         break
#     i+=1
#     print(i)

# for i in "string":
#     if i=="r":
#         break
#     print(i)


# for i in "string":
#     if i=="i":
#         continue
#     print(i)


# for i in range(1,11):
#     print(i)


# a=[1,3,5,7,8,10]
# i=1
# while i<=10:
#     if i not in a:
#         print(i)
#     i+=1

# a=["q","z"]
# num=int(input("enter num : "))
# i=1
# while i<=num:
#     j=1
#     while j<=num:
#         j=j+1
#     print('"',"q",i,'"','"',"z",i,'"')
#     print()
#     i=i+1

# num=int(input("enter the number: "))
# a={}
# for i in range(num+1):
#     x=num*i
#     a.update({i:x})
# print(a)

# a={"e":3,"b":6,"c":34,"d":10}
# i=None
# j=-1
# for k in a:
#     if  i is None or i <a[k]:
#         i=a[k]
#         j=k
# print(k)

# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# d3={}
# sum=0
# for x in d1:
#     if x in d2:
#         sum=d1[x]+d2[x]
#         d1[x]=sum
#         d2.pop(x)
# d1.update(d2)
# print(d1)

# o=["monika","dad","mom"]
# a=[]
# b=[]
# c=[]
# for i in range(len(o)):
#     for j in range(len(o[i])):
#         if i==0:
#             a.append(o[i][j])
#         if i==1:
#            b.append(o[i][j])
#         if i==2:
#             c.append(o[i][j])
# print(a)
# print(b)
# print(c)
# x=a[::-1]
# y=b[::-1]
# z=c[::-1]
# count=1
# if a==x:
#     print(x,count,"palindrom")
#     count=count+1
# if b==y:
#     print(y,count,"it is palindrim")
#     count=count+1
# if c==z:
#     print(z,count,"it is palindrom")



# a=[1,3,"5",8,"6",3,"2",2.5,"2.3",3+6j]
# i=0
# b=[]
# while i<len(a):
#     if type (a[i])==complex:
#         b.append(a[i])
#     i=i+1
# print(b)


# list=[1,2,3,1,2,3]
# b=[]
# i=0
# while i<len(list):
#     j=i+1
#     while j<len(list):
#         if list[i]==list[j]:
#             del list[j]
#             b.append(list[i])
#         j=j+1
#     i=i+1
# print(b)

# for i in list:
#     if i not in b:
#         b.append(i)
# print(b)



# a=["vaishnavi"]
# i=0
# for i in a:
#     a=i[::-1]
# print(a)



# a=["vaishu","bhagu","dhanu","grecy"]
# b=[3,4,2,1]
# dict={}
# for i in range(len(a)):
#     dict[a[i]]=b[i]
# print(dict)

# a=["vaishnavi"]
# i=0
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)
#     print(b)


# a=input("enter name")
# if "ok" in a:
#     print(a+"ly")
# elif "ly" in a:
#     print(a+"ing")
# else:
#     print(a+"okly")


# a=input("enter the name")
# lis=list(a)
# print(lis)
# for i in range(len(lis)):
#     print(lis[i].upper()+(i+1)*lis[i])
# print("__",lis.join(lis[i]))


# num=input("enter the name")
# if "o" in num:    
#     print(num+"li")
# if "k" in num:
#     print(num+"li")
# else:
#     print(num+"li")

# i=1
# while i<=10:
#     if i%2==0:
#       print(i,"even number")
#     else:
#         print(i,"od number")
#     i=i+1


# s=1
# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end=" ")
#         j=j+1
#     k=1
#     while k<=s:
#         print("*",end=" ")
#         k=k+1
#     s=s+2
#     print()
#     i=i+1

# a=input("enter the name")
# b=(a[:-2])+"ly"
# print(b)


# def number (num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# number(8)


# i=1
# while i<=10:
#     print(i)
#     if (i==5 )and (i==6):
#       continue
#     i=i+1
# i=i+1



# a=[1,2,3,4,5]
# i=0
# while i<len(a):
#     i=i+1
# print(a[::-1])
# # b=len(a)-1
# # while i<=b:
# #     k=a[i]
# #     a[i]=a[b]
# #     a[b]=k
# #     i=i+1
# #     b=b-1
# # print(a)


# i=11
# while i>=0:
#     i=i-1
#     if i==5 or i==6:
#        continue
    
#     print(i)
#     # i=i+1
    

# def function(a,b,c=4):
#     print("right")
# function(5)

# from os import close
# from typing import ()
# f=close()



# f=open("demofile.text",'a')
# f.write("vaishu") 

# a=[[1,2,3],[6,5,4],[9,8,7]]
# i=0
# while i<len(a):
#     b=0
#     j=0
#     while j<len(a[i]):
#         if a[i][j]>b:
#             b=a[i][j]
#         j=j+1
#     print(b)
#     i=i+1


# def disp():
#     def show():
#         print("right")
#     print("yes")
#     show()
# disp()


# a=2
# b=3
# b=(a+b)
# c=b/2
# print(type(c))

# a=["vaishnavi"]
# # b={}
# for i in a:
#     c=i[::-1]
# print(c)

# a=[1,2,3,4]
# b={}
# for i in a[::-1]:
#     b=({i:b})
# print(b)

# f=open("demofile.text",'r')
# var=f.read()
# print(var)
# import json
# a={1:2,3:5}

# with open("mona",'w')as file:
#     json.dump(a,file,indent=4)

# import json
# a={2:4,6:8,3:5,8:3}
# b=json.dumps(a)
# print(type(b))
# b=json.(a)
# print(b)

# a=[{"math": 67,"sci": 45},{"math":90,"sci":45},{"math":95,"sci":85}]
# num=input("enter the subject: ")
# b=[]
# for i in a:
#     b.append(i[num])
# print(b) 

# a={"a":200,"b":900,"d":600,"e":400} 
# b={"a":400,"b":800,"d":900,"k":200}
# # c={} 
# for i in b:
#     if i in a:
#         a[i]=a[i]+b[i]
#     else:
#         a[i] =b[i] 
# print(a)        

# a=[2,3,4,5,6]
# b=[3,4,5,6,7]
# print(a+b)

# num_list=[]
# list_length=int(input("enter the number"))
# for i in range(list_length):
#     value=int(input("enter valueof ele ments"))
#     num_list.append(value)
# for i in range(list_length):
#     for j in range(list_length):
#         if num_list[i]<num_list[j]:
#             temp=num_list[i]
#             num_list[i]=num_list[j]
#             num_list[j]=temp
# print("asscending",num_list)



# a=[1,2,3,4]
# b={}
# for i in a[::-1]:
#     b=({i:b})
# print(b)
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

# a=[{"math":20,"sec":35},{"math":21,"sec":31},{"math":22,"sec":33}]
# num=input("enter the subject")
# b=[]
# for i in a:
#     b.append(i[num])
# print(b)


# i=10
# while i>=0:
#     print(10-i)
#     i=i-1
# num=123
# a=(num//10)
# print(a)


# s=[7,6,5,4,3,2,1]
# i=0
# b=[]
# for i in range(len(s)):
#     if s[i]%2==0:
#         pass
#     else:
#         b.append(s[i])
# print(b)       
# i=0
# for i in range(len(b)):
#     j=i
#     temp=0
#     for j in range(len(b)):
#         if b[j]>b[i]:
#             temp=b[i]
#             b[i]=b[j]
#             b[j]=temp
# i=0
# for i in range(len(s)):
#     if s[i]%2==0:
#         a=s.index(s[i])
#         b.insert(a,s[i])
# print(b)