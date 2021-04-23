t = int(input())
for i in range(t):
    n = int(input())
    digit_sum = 0
    while(n>0):
        digit_sum = digit_sum + (n%10)
        n = int(n/10)
    print(digit_sum)
