import random
rn = random.randrange(1, 101, 1)
num = -1
cnt = 0
while True :
  n = int(input("숫자 입력: "))
  cnt = cnt+1
  if(n < rn):
    print("up")
    continue
  elif(n > rn):
    print("down")
    continue
  elif(n == rn):
    print("정답!",cnt,"번 만에 맞추었네요.")
    break
