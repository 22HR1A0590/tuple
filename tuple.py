# tuple

'''1) Write a program to get the tuple elements and print it.
Sample Input:
3
20
10
30
Sample Output:
(20, 10, 30)'''

Ans:
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(tuple(lst))

'''2) Write a program to get the elements of tuple in a single line separated by space and print the tuple values.
Sample Input:
20 10 30
Sample Output:
20, 10, 30'''

Ans: 
a=map(int,input().split())
b=tuple(a)
print(b)

'''3) Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3'''

Ans:
elements = input().split()
tuple_elements = tuple(map(int, elements))
print(len(tuple_elements))

'''4) Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60'''

Ans:
n = int(input())
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
tuple_elements = tuple(elements)
total_sum = sum(tuple_elements)
print(total_sum)

'''5) Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30'''

Ans:
n = int(input())
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
tuple_elements = tuple(elements)
max_value = max(tuple_elements)
print(max_value)

'''6) Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10'''

Ans:
n = int(input())
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
tuple_elements = tuple(elements)
min_value = min(tuple_elements)
print(min_value)

'''7) Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4'''

Ans:
elements = input().split()
tuple_elements = tuple(map(int, elements))
x = int(input())
count = tuple_elements.count(x)
print(count)

'''8) Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60'''

Ans:
elements = input().split()
tuple_elements = tuple(map(int, elements))
total_sum = 0
for element in tuple_elements:
    total_sum += element
print(total_sum)

'''9) Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd'''

Ans:
elements = input().split()
even_count = 0
odd_count = 0
for element in elements:
    number = int(element)  
    if number % 2 == 0:    
        even_count += 1
    else:                  
        odd_count += 1
if even_count > odd_count:
    print("Even")
elif odd_count > even_count:
    print("Odd")
else:
    print("Equal")

'''10) Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6'''

Ans:
elements = input().split()
tuple_elements = tuple(map(int, elements))
x = int(input())
count = tuple_elements.count(x)
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
factorial_value = calculate_factorial(count)
print(factorial_value)



















