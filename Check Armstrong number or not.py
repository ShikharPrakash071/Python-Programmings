print("Check wheteher a number is Armstrong number or not\n");

a=int(input("Enter a number to see whether it is a Armstrong number or not: "));
orig=a
sum=0
while(a>0):
    sum=sum+(a%10)*(a%10)*(a%10)
    
    a=a//10
if(orig==sum):
     print("The chosen number",orig,"is a Armstrong number");
else:
     print("The chosen number",orig,"is not a Armstrong number");