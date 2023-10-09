text = input("Enter the text to test: ")
reverse = ""
y = len(text) - 1

while y >= 0:
    reverse = reverse + text[y]

    y = y - 1
if text == reverse:
    print("the text is plindrome")

else:
    print("the text is not plindrome")
