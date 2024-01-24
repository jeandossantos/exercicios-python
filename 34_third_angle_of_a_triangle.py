"""You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
"""

def other_angle(a, b):
  return 180 - (a + b)

print(other_angle(30, 60)) # 90
print(other_angle(20, 80)) # 80
print(other_angle(100, 60)) # 20