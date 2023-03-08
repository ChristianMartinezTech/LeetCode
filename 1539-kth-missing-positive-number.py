#!/usr/bin/env python3

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

# Armar un array de numeros que no estan en arr
# Hasta que len(missing-arr) == k

arr = [2,3,4,7,11]
k = 5
missing_elem = [item for item in range(1, arr[-1] + 2) if item not in arr]
 
try:
    print(missing_elem[k-1])

except IndexError:
    if (len(missing_elem) - 1) < k:
        for i  in range((missing_elem[-1]) + 1, (missing_elem[-1] + k)):
            missing_elem.append(i)
    
    print(missing_elem[k-1])