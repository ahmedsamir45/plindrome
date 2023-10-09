text = input("Enter a word to test: ")

reverse = ""
for i in range(len(text) - 1, -1, -1):
    reverse += text[i]

if text == reverse:
    print("the text is plindrome")

else:
    print("the text is not plindrome")
