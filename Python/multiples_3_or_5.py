

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    def sum_div(k):
        m = (n-1) // k
        return k * m * (m+1) // 2
    total = sum_div(3) + sum_div(5) - sum_div(15)
    print(total)
