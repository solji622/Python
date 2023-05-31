#1부터 입력받은 수까지 각각의 제곱 구하기
n = int(input("정수 입력: "))
i = 1
while i<=n :
  print(i, i*i)
  i = i+1
  
  
#100까지의 정수 중 8의 배수이면서 12의 배수가 아닌 것만 출력하기
i = 0;
while i <= 100 :
  if i % 8 == 0 and i % 12 != 0 :
    print(i)
  i = i+1
