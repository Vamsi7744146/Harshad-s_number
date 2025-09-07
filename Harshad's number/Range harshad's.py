#wrie a program harshad's number in given range
LL=int(input())
UL=int(input())
for num in range(LL,UL+1):
    summ=0
    dummy=num
    while dummy>0:
        rem=dummy%10
        summ+=rem
        dummy//=10
    if num%summ==0:
        print(num)
