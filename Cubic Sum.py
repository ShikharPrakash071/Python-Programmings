print("Sum of cube of digits of a given number\n");

a=int(input("Enter a three digit number to see its cubic sum of each digit: "));
sum=0
while(a>0):
    sum=sum+(a%10)*(a%10)*(a%10)
    a=a//10
print("The cubic sum of digit of number inputed is :",sum);