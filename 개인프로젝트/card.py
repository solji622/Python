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
print("2. 출력된 카드가 사라진 뒤 나타나는 정답입력란에 위치를 입력한다.")
print("3. 정답이면 1점이 추가되고 오답이면 1점이 줄어든다.")
print("4. 누적 점수 3점이 되면 게임이 종료된다.")
print("")

# 랜덤 위치에 한쌍의 카드 넣기
for i in range(len(card)):
  # 첫번째 요소에 세가지 출력되는 오류 고치기
  if rn1 == 0 or rn1 == 1 or rn1 == 2:
    print(" ■ ", end="")
  else:
    print(" □ ", end="")
  for j in range(len(card)-1):
    print(" □ ", end="")
    if j == 1:
      print("")
  print("")

# output.clear()
