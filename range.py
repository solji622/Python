n = int(input("input the number: "))
for i in range(1, n+1): #1부터 n(입력해둔 숫자)까지 / n에는 +1씩
    if i % 3 == 0 :
        print(i, ": 3의 배수") #범위에 해당하는 숫자 중 조건에 만족하는 숫자만 출력