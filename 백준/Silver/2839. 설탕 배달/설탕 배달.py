n = int(input())
q, r = divmod(n, 5) # 몫, 나머지
result = -1
if r > 0: # 나머지가 있으면
    if r % 3 == 0: # 3으로 나누어 떨어지면 이게 최소값
        result = q + r // 3
    else: # 3으로 안나눠지면 5를 쪼개서 다시 계산
        for i in range(q - 1, 0, -1): # 5를 1개씩 넣어봐야함
            r = n - (i * 5)
            if r % 3 == 0: # 남은게 3으로 나눠지면 끝 
                result = i + r // 3
                break

        #안나눠지면 n을 3으로 나눠줌
        if result == -1 and n % 3 == 0:
            result = n // 3
else:
    result = q
print(result)