count = 0
t = int(input())
tc = 0  # testCase

while k > tc:
    n, k = map(int, input().split())
    str_input = input().strip()
    count = 0
    for i in range(len(str_input)//2):
        if str_input[i] != len(str_input)-i+1:
            count += 1
    ans = abs(k - count)
    tc += 1

print('case #' + str(tc)+': '+str(ans))
