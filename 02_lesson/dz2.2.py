a = int(input("Please enter five digit number:"))
b = ((a%10*10000) + (a//10%10*1000) + (a//100%10*100) + (a//1000%10*10) + a//10000)
print(b)