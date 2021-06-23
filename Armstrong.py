print("Program to print Armstrong Numbers\n");
n=int(input("Enter any number: "));
i=n
count=0
while(i>0):
    i=i//10
    count=count+1
sum=0
i=n
while(i>0):
    digit=i%10
    x=1
    pro=1
    while(x<=count):
        pro=pro*digit
        x=x+1
    sum=sum+pro
    i=i//10

if(sum==n):
    print("The given number",n,"is an armstrong number");
else:
    print("The number is not an armstrong number");