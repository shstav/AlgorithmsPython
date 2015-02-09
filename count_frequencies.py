"""
You are given an array of n integers which can contain integers from 1 to n only.
Some elements can be repeated multiple times and some other elements can be absent from the array.
Write a running code on paper which takes O(1) space apart from the input array and O(n) time to
print which elements are not present in the array and the count of every element which is there
in the array along with the element number.
NOTE: The array isn't necessarily sorted.u

>>> a
[2, 3, 3, 1, 3]
>>> count_frequencies(a)
The number 1 appears 1 times
The number 2 appears 1 times
The number 3 appears 3 times
The number 4 appears 0 times
The number 5 appears 0 times
"""

def count_frequencies(a):
  index = 0
  while index < len(a):
    value_at_index = a[index]
    if 0 < value_at_index:
      if 0 < a[value_at_index-1]:
        a[index] = a[value_at_index-1]
        a[value_at_index-1] = -1
      else:
        a[value_at_index-1] -= 1
        a[index] = 0
        index += 1
    else:
      index += 1
  print_results(a)


def print_results(a):
  for index, value in enumerate(a):
    string_formating_values = {"number" : index + 1, "count": -value}
    print "The number %(number)s appears %(count)s times" % string_formating_values


