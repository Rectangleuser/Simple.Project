sum = 0
ind = 1

while (True):
    num = input("Enter a number: ")
    if str(num) != 'q':
        sum = sum + int(num)
        print(num, "\t\t\t\t\t[" + str(ind) + "]")
        ind = int(ind)+1
    else:
        print("Ans","=",sum)
