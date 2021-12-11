# i=156
# while i<=246:
#     x=i-145
#     print(x)
#     i=i+1


# name=input("Enter the name : ")
# if("ing" in name):
#     print(name[0:-3]+"ly")
# elif("ly" in name):
#     print(name[0:-2]+"ing")
# else:
#     print(name+"ing"+"ly")

# number_string=input("enter the number :")
# if number_string+[::-1] :
#     print(number_string[::-1])

# a=[1,2,3,4,5,[6,7,8]]   #make a flat list.
# b=[]
# i=0
# while i<len(a):
#     if type(a[i]) is list:
#         j=0
#         while j <len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)

# user=int(input("number: "))  # check second number is 3 or not if second number is 3 print yes.
# a=(user//100)%10
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
#     # print(b)
#     c.update(b)
# print(c)

# a=[1,2,1,3,4,3,4,3,2,5,2,2,1]
# b={}
# for i in a:
#     d=a.count(i)
#     e=d//2
#     b.update({i:e})
# #     b[i]=d
# # print(b)
# print(b)

# def string…
# _123var=1
# print(_123var)

# list=["subreena"]
# for i in list:
#     a=i[::-1]
# print(a)

# user=int(input("enter a number:"))
# a={}
# b={}
# i=0
# while i<user:
#     name=input("enter ur name: ")
#     age=int(input("enter ur age: "))
#     a[name]=age
#     b[i+1]=a
#     i+=1
# print(b)

# user=int(input("enter a number:"))
# a={}
# b={}
# i=0
# while i<user:
#     name=input("enter ur name: ")
#     age=int(input("enter ur age: "))
#     a[name]=age
#     i+=1
# print(a)


# list=[11,12.9,3,11,"python","js"]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==str:
#         # print(list[i])
#         a.append(list[i])
#     i+=1
# print(a)
# user1=int(input("enter num : "))
# user2=int(input("number: "))
# user3=int(input("number: "))
# if user1>user2:
#     print(user1,"greater")
# elif user2>user3:
#     print(user2,"greater")
# else:
#     print(user3,"graeter")


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# i=4
# j=0
# while i<len(a):
#     if j==0:
#         a[i]=15
#         j=1
#     else:
#         a[i]=20
#         j=0
#     i+=5
# print(a)


# a=[[1,2,3,4],[5,6,7,8],[8,9,10]]
# list=[]
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if j==0:
#             sum=sum+a[i][j]
#         elif j==1:
#             sum1=sum1+a[i][j]
#         elif j==2:
#             sum2=sum2+a[i][j]
#         elif j==3:
#             list.append(a[i][j])
#         j+=1
#     i+=1
# list.append(sum)
# list.append(sum1)
# list.append(sum2)
# print(list)


# i=100
# sum=0
# while i>0:
#     sum=sum+i
#     i-=1
# print(sum)


# list=["a","b","c","d","a","c","d","e","f","a","b"]
# i=0
# o=0
# while i<len(list):
#     if list[0]==list[i]:
#         k=(i)
#     elif list[1]==list[i]:
#         l=(i)
#     elif list[2]==list[i]:
#         m=(i)
#     elif list[3]==list[i]:
#         n=(i)
#     elif list[7]==list[i]:
#         o=(i)
#     elif list[8]==list[i]:
#         p=(i)
#     i+=1
# print(list[0],":",k,list[1],":",l,list[2],":",m,list[3],":",n,list[7],":",o,list[8],":",p)

# a=[1,2,3,4,5,6,7,8,9,10]
# c={}
# for i in a:
#     b={}
#     for j in range(0,i):
#         s=i*5
#         b.update({i:s})
#     c.update(b)
# print(c)

# list=[1,0,0,1,1,0,1,1]
# list= [1, 0, 0, 2, 1]
# a=0
# sum=0
# i=1
# while i<=len(list):
#     b=list[-i]
#     sum=sum+(2**a)*b
#     a=a+1
#     i=i+1
# print(sum)

