'''
Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
'''

"""
Using “in” Statement 
Using a loop 
"""

#1 Using “in” Statement 
list=[1, 6, 3, 5, 3, 4]
search=4

if search in list:
    print("exist")
else:
    print("not exist")

#2 Using a loop 
for i in list:
    if(i==search):
        print("exist")
        i=1
    else:
        i=-1
if(i==-1):
    print("not exist")

