'''
Input: [2, 3, 5, 6, 7]
Output: []
Explanation: Python list is cleared and it becomes empty so we have returned empty list.
'''
"""
Using clear()
Reinitializing the list
Using “*= 0”
Using del
Using pop() method
Using slicing
"""

#1 Using clear() method
list=[2, 3, 5, 6, 7]
list.clear()
print(list)

#2 Reinitializing the list
list=[2, 3, 5, 6, 7]
list=[]
print(list)

#3 Using “*= 0”
list=[2, 3, 5, 6, 7]
list*=0
print(list)

#4 Using del
list=[2, 3, 5, 6, 7]
del list[:]
print(list)

#5 Using pop() method
list=[2, 3, 5, 6, 7]
while(len(list)!=0):
    list.pop()
print(list)

#5 Using slicing
list=[2, 3, 5, 6, 7]
list=list[:0]
print(list)