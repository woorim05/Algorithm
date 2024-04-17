n = int(input())
num_count = {1:0, 2:1} # 숫자에 대한 횟수 딕셔너리

for i in range(3, n + 1):
    num_count[i] = num_count[i - 1] + 1 # 3번 연산
    
    if i % 3 == 0: # 1번 연산과 3번 비교
        num_count[i] = min(num_count[i // 3] + 1, num_count[i])
    
    if i % 2 == 0: # 2번 연산 위의 결과랑 비교
        num_count[i] = min(num_count[i // 2] + 1, num_count[i])
        
print(num_count[n])