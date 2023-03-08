#!/usr/bin/env python3

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

# Vamos a evaluiar la condicion de (), [] y {} dentro de el string y borrarlos
# los (), [] y {} se van a ir eliminando desde adentro

while '()' in s or '[]'in s or '{}' in s:
    s = s.replace('()','').replace('[]','').replace('{}','')

if len(s) == 0:
    return True
else:
    return False
