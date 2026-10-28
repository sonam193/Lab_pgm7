
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

s = input("Enter a string: ")

if is_palindrome(s):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
