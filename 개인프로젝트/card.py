from google.colab import output
import random

# 3 * 3의 2차원 배열 선언
row, col = 3, 3
card = [[None] * col for i in range(row)]
rn1 = random.randrange(len(card))
rn2 = random.randrange(len(card))

#ANSI 코드를 사용하여 글씨를 굵게 출력
print('\033[1m' + "« 카드 짝 맞추기 »"+ '\033[0m')
print("")

# 기본 카드 출력
for i in range(len(card)):
  print(" □ ", end="")
  for j in range(len(card)-1):
    print(" □ ", end="")
    if j == 1:
      print("")
  print("")

# 게임 방법
print("1. 9개의 빈카드에서 랜덤으로 등장하는 한쌍의 카드의 위치를 기억한다.")
print("2. 출력된 카드가 사라지고 정답입력란에 위치(배열의 인덱스값)를 입력한다.")

# 랜덤 위치에 한쌍의 카드 넣기

# output.clear()
