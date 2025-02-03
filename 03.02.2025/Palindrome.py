def is_palindrome(s):
    return s == s[::-1]


input_str = input("Enter a string: ")


if is_palindrome(input_str):
    print(input_str, "is a palindrome")
else:
    print(input_str, "is not a palindrome")
