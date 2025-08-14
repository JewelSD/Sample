def amstrong():
    num=int(input("Enter the number:"))
    num1=str(num)
    length=len(num1)
    res=sum(int(digit)**length for digit in num1)
    print (res)
    result=num==res
    if(result):
        print("The number is amstrong")
    else:
        print("Not amstrong")

amstrong()