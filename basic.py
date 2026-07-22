1. WAP to print happy and sad number 

num=13
while (num!=1 and num!=4):
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    num=sum

if num==1:
    print("Happy Number :)")
else:
    print("Sad Number :(")


2. WAP to print Armstrong number or not

num=int(input("Enter the number:"))
sum=0
temp=num
while (temp>0):
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if num==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")


3. WAP to print perfect no or not

num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
        
if sum==num:
    print("Perfect no")
else:
    print("Not Perfect no")


4. WAP to print palindrome no

num=int(input("Enter the number:"))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
        
if original==rev:
    print("Palindrome no")
else:
    print("Not Palindrome no")
