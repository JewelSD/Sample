def palin():
    word=input("Enter the word to check:")
    pali=word[::-1]
    result=word==pali
    if(result):
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")

palin()