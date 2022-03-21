문제 https://www.acmicpc.net/problem/1026
    

    
풀이1

n = int(input())

data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))
result = 0

a = sorted(data_1, reverse= True)
b = sorted(data_2)

for i in range(n):
    result += a[i] * b[i]

print(result)


느낀점

두 번째 배열에 있는 것은 정렬하면 안된다는 조건을 무시하고 푼 풀이지만 백준에서는 정답 처리한 문제이다.


풀이2

n = int(input())

data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))
result = 0


for i in range(n):
    result += min(data_1) * max(data_2)
    data_1.pop(data_1.index(min(data_1)))
    data_2.pop(data_2.index(max(data_2)))

print(result)

느낀점
pop과 index를 활용하여 푼 풀이이며 기본 문법을 까먹었지만 상기시킨 문제이다.
