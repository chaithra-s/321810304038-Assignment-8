#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

def swap(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(swap('abc', 'xyz'))

#Write a Python program to remove a newline in Python.
str1='Python\n'
print(str1)
print(str1.rstrip())

#Write a Python program to perform Deletion of a character 
s1="apple"
print(s1)
print(s1[1:])

#Write a program to print every character of a string entered by user in a new line using loop. 
s="mango"
for i in s:
	print(i)
