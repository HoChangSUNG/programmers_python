def solution(n, money):#거스름돈
    table = [[0] * (n+1) for _ in range(len(money))]
    table[0][0] = 1
    for i in range(money[0], n+1, money[0]):
        table[0][i] = 1
    for r in range(1, len(money)):
        for c in range(n+1):
            if c >= money[r]:
                table[r][c] = (table[r-1][c] + table[r][c-money[r]]) % 1000000007
            else:
                table[r][c] = table[r-1][c]
    return table[-1][-1]

n = 6
money = [2,3]
solution(n,money)