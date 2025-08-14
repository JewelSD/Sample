def palin():
    done=input("Enter the word:")
    pali=done[::-1]
    result=done==pali
    if(result):
        print(f"{done} is palindrome")
    else:
        print(f"{done} is not palindrome")

palin()