n=int(input())
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    summ+=rem
    dummy//=10
if n%summ==0:
    print('n is harshads number')
else:
    print('n is not harshad number')