def process_numbers(numbers):
"""
Process a list of integers by multiplying even numbers by 2
and odd numbers by 3.


Parameters
----------
numbers : list[int]
A list of integers to process.


Returns
-------
list[int]
A new list containing processed integers.
"""
# Use list comprehension for concise and pythonic transformation
return [num * 2 if num % 2 == 0 else num * 3 for num in numbers]




def transform_strings(strings):
"""
Transform a list of strings by converting long strings (length > 5)
to uppercase and short strings to lowercase.


Parameters
----------
strings : list[str]
A list of strings to transform.


Returns
-------
str
A single space-separated string of transformed values.
"""
# Inline comment explaining list comprehension expression
# Join results into a single string after transformation
return " ".join([s.upper() if len(s) > 5 else s.lower() for s in strings])




def main():
"""
Demonstrate numeric and string processing functions using
example input lists.
"""
number_list = [1, 2, 3, 4, 5, 6, 7]
fruit_list = ["apple", "banana", "kiwi", "grapefruit", "cherry"]


processed_nums = process_numbers(number_list)
processed_strings = transform_strings(fruit_list)


print("Processed Numbers:", processed_nums)
print("Processed Strings:", processed_strings)




if __name__ == "__main__":
main()
