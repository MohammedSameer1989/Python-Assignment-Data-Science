#!/usr/bin/env python
# coding: utf-8

# In[1]:


Q1. Explain with an example each when to use a for loop and a while loop.
Ans-A for loop is typically used when you know beforehand how many times you want to iterate or when you want to iterate over a collection (e.g., a list, tuple, or range) of items a specific number of times. It's great for situations where you have a clear idea of the iteration count.
and While Loop:
A while loop, on the other hand, is used when you want to continue iterating as long as a certain condition is met. It's suitable for situations where you don't know the exact number of iterations in advance and need to keep iterating until a specific condition becomes False.


# ##Write a python program to print the sum and product of the first 10 natural numbers using for
# and while loop.

# In[3]:


l=[1,2,3,4,5,6,7,8,9,10]


# In[4]:


result=0
for i in l:
    result=result+i
result    


# In[6]:


n = 10
sum_natural = 0
product_natural = 1

for i in range(1, n + 1):
    sum_natural += i
    product_natural *= i

print(f"Sum of the first {n} natural numbers is: {sum_natural}")
print(f"Product of the first {n} natural numbers is: {product_natural}") 


# In[7]:


n = 10
sum_natural = 0
product_natural = 1
i = 1

while i <= n:
    sum_natural += i
    product_natural *= i
    i += 1
print(f"Sum of the first {n} natural numbers is: {sum_natural}")
print(f"Product of the first {n} natural numbers is: {product_natural}")    


# In[10]:


###Create a python program to compute the electricity bill for a household.


The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
You are required to take the units of electricity consumed in a month from the user as input.
Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250.

units_consumed = int(input("Enter the units of electricity consumed in a month: "))

total_bill = 0

if units_consumed <= 100:
    total_bill = units_consumed * 4.5
elif units_consumed <= 200:
    total_bill = (100 * 4.5) + ((units_consumed - 100) * 6)
elif units_consumed <= 300:
    total_bill = (100 * 4.5) + (100 * 6) + ((units_consumed - 200) * 10)
else:
    total_bill = (100 * 4.5) + (100 * 6) + (100 * 10) + ((units_consumed - 300) * 20)
    
print(f"Total electricity bill for {units_consumed} units is: Rs. {total_bill}")


# In[ ]:


###Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list.


# In[12]:


result_list = []

for num in range(1, 101):
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        result_list.append(num)


print(result_list)


# In[ ]:


###Write a program to filter count vowels in the below-given string.
string = "I want to become a data scientist"


# In[13]:


string = "I want to become a data scientist"

vowel_count = 0
vowels = set("aeiouAEIOU")


for char in string:
    # Check if the character is in the set of vowels
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")


# In[ ]:





# In[ ]:




