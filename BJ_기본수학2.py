import sys

input = sys.stdin.readline

n = int(input())

numbers = map(int, input().split())

sosu = 0

for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1 # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1 # error가 없으면 소수

print(sosu)


#2

import sys

input = sys.stdin.readline

start_num = int(input())
last_num = int(input())

sosu_list = []

for num in range(start_num, last_num+1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break # 2부터 num - 1까지 나눈 몫이 0이면, error 가증가하고 for 문을 끝냄
        if error == 0:
            sosu_list.append(num)

if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)


#3

import sys

input = sys.stdin.readline

num = int(input())

while num != 1:
    for i in range(2, num + 1):
        # 나눠지면 출력하고,
        # 다음을 위해 해당 수로 num을 나눠줍니다.
        if (num % i == 0):
            print(i)
            num = num // i
            break


#4

def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if isprime(i):
        print(i)


#5

def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

all_list = list(range(2, 24912))
memo = []

for i in all_list:
    if isprime(i):
        memo.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in memo:
        if n < i < 2 * n:
            count += 1
    print(count)
    n = int(input())

