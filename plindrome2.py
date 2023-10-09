def is_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


x = input("Enter a word to test: ")
if is_palindrome(x) == True:
    print(f"{x} is plindrome")

else:
    print(f"{x} is not plindrome")
