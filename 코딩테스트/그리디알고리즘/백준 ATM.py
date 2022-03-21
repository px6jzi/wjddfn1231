백준 알고리즘

문제: https://www.acmicpc.net/problem/11399

풀이:

n = int(input())
data = list(map(int, input().split()))
result = 0


for i in range(n):
    for j in range(i+1):
        data.sort()
        result = result + data[j]

print(result)

느낀점:
 
전형적인 그리디 알고리즘 문제이다. 정렬을 하고 값을 누적해나가는 방식이기에 이중 for문을 이용해 누적값 계산하도록 코드를 작성했다.
