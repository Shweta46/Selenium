'''
Q1. print two numbers that occurs in a array single time but the other elements appear twice do it
without taking any extra space and linear time complexity
Input:
1 2 1 2 4 5
Output:
4 5
'''

n = [1, 2, 1, 2, 4, 5]
def print_once(n):
    l = len(n)
    for i in range(l):
        if n[i] not in (n[:i] + n[i+1:]):
            print(n[i])

print(print_once(n))

'''
Q2. check parantheses are correct or not (properly closed or not)
input:
((()))
()()()
(()(
output:
true
true 
false
'''


