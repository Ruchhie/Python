'''
Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1
'''
#1  if-else statement 

def Maximum(a,b):
    if(a>b):
        return a
    else:
        return b
    
a=54
b=20

print(Maximum(a,b))

#2 max() function
Maximum=max(a,b)
print(Maximum)

#3 Ternary Operator
print(a if a>=b else b)

#4 lambda function 
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} maximum number')

#5 list comprehension
x=[a if a>b else b]
print(x)

#6 sort() method
x=[a,b]
x.sort();
print(x[-1])