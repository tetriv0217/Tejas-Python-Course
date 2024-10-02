# Sample string for demonstration
s = "Hello, World!"
number_str = "12345"
mixed_str = "Hello123"
whitespace_str = "  Hello  "
title_str = "hello world"

# 1. len() - Returns the length of a string
print(len(s))  # Output: 13

# 2. lower() - Converts all characters to lowercase
print(s.lower())  # Output: "hello, world!"

# 3. upper() - Converts all characters to uppercase
print(s.upper())  # Output: "HELLO, WORLD!"

# 4. strip() - Removes leading and trailing whitespaces
print(whitespace_str.strip())  # Output: "Hello"

# 5. replace() - Replaces occurrences of a substring with another substring
print(s.replace("World", "Python"))  # Output: "Hello, Python!"

# 6. split() - Splits the string into a list using whitespace as the default delimiter
print(s.split())  # Output: ['Hello,', 'World!']

# 7. join() - Joins a list of strings with a specified separator
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"

# 8. find() - Returns the index of the first occurrence of a substring
print(s.find("World"))  # Output: 7

# 9. count() - Returns the number of occurrences of a substring
print(s.count("l"))  # Output: 3 (There are three 'l's in "Hello, World!")

# 10. startswith() - Checks if the string starts with a specific prefix
print(s.startswith("Hello"))  # Output: True

# 11. endswith() - Checks if the string ends with a specific suffix
print(s.endswith("World!"))  # Output: True

# 12. isnumeric() - Checks if all characters in the string are numeric
print(number_str.isnumeric())  # Output: True

# 13. isdigit() - Checks if all characters in the string are digits
print(number_str.isdigit())  # Output: True

# 14. isalnum() - Checks if all characters in the string are alphanumeric
print(mixed_str.isalnum())  # Output: True

# 15. capitalize() - Capitalizes the first character of the string
print(title_str.capitalize())  # Output: "Hello world"

# 16. title() - Capitalizes the first character of each word
print(title_str.title())  # Output: "Hello World"

# 17. swapcase() - Swaps the case of all characters in the string
print(s.swapcase())  # Output: "hELLO, wORLD!"

# 18. zfill() - Pads the string with zeros on the left until the specified width is reached
number_str_short = "42"
print(number_str_short.zfill(5))  # Output: "00042"
