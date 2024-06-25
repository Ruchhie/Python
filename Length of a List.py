#Input: lst = [10,20,30,40]
#Output: 4
#Explanation: The output is 4 because the length of the list is  4.

'''
Using len() function
Using Naive Method
Using length_hint()
Using sum() method
Using a list comprehension
Using recursion
Using enumerate function
Using Collections Module
'''
#1 Using len() function
list=[10,20,30,4,5,6,7]
size=len(list)
print(size)

#2 Using Naive Method
counter=0
for i in list:
    counter+=1
print(counter)

#3 Using length_hint()
from operator import length_hint
list_len_hint = length_hint(list)
print("Length of list using length_hint() is : " + str(list_len_hint))

#4 Using sum() method
leng=sum(1 for i in list)
print(leng)

#5 Using a list comprehension
leng=sum(1 for _ in list)
print(leng)

#6 Using recursion
def count_recursion(list):
    if not list:
        return 0
    return 1 + count_recursion(list[1:])

print(count_recursion(list))

#7 Using enumerate function
s=0
for i in enumerate(list):
    s+=1
print(s)

#8 Using Collections Module
from collections import Counter
len=sum(Counter(list).values())
print(len)
