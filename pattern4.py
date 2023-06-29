rows=int(input("enter value : "))
ascii=int(input("enter ascii : "))
for i in range(0,rows):
    for j in range(0,i+1):
        val=chr(ascii)
        print(val,end=" ")
        ascii=ascii+1
    print()