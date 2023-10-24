from google.colab import output
#vs로 코딩할 경우
#import os / os.system('cls')
import random

# 길이 9의 1차원 배열 선언
card = [0 for i in range(9)]
score = 0

# 랜덤 숫자 뽑는 함수
def random_num():
  rn1 = random.randrange(len(card))
  rn2 = random.randrange(len(card))

  while rn1 == rn2:
    rn2 = random.randrange(len(card))

  return rn1, rn2

while True:
  rn1 = None
  rn2 = None
  rn1, rn2 = random_num()

  #ANSI 코드를 사용하여 글씨를 굵게 출력
  print('\033[1m' + "« 카드 짝 맞추기 »"+ '\033[0m')
  print("")

  # 기본 카드 출력
  for i in range(len(card)):
    print(" □ ", end="")
    if i == 2 or i == 5 or i == 8:
      print("")
  print("")

  # 게임 방법
  print("** 게임 방법 **")
  print("1. 9개의 빈카드에서 랜덤으로 등장하는 한쌍의 카드의 위치를 기억한다.")
  print("2. 출력된 카드가 사라진 뒤 나타나는 정답입력란에 위치를 입력한다.")
  print("3. 정답이면 1점이 추가되고 오답이면 1점이 줄어든다.")
  print("4. 누적 점수 3점이 되면 게임이 종료된다.")
  print("")

  # 랜덤 위치에 한쌍의 카드 넣기
  for i in range(len(card)):
    card[rn1] = rn1
    card[rn2] = rn2
    if card[i] == rn1 or card [i] == rn2:
      print(" ■ ", end="")
      if i == 2 or i == 5 or i == 8:
        print("")
    else:
      print(" □ ", end="")
      if i == 2 or i == 5 or i == 8:
        print("")

  # 출력문 지우기
  clear_num = int(input('카드를 지워주세요 [0]: '))
  if clear_num == 0:
    output.clear()

  # 짝 맞추기
  for i in range(len(card)):
    print(" □ ", end="")
    if i == 2 or i == 5 or i == 8:
      print("")
  print("")

  print("카드 위치는 왼쪽에서 오른쪽으로")
  print("0 1 2 | 3 4 5 | 6 7 8")
  print("입니다. 정답을 입력해주세요")

  correct1 = int(input('정답[1]: '))
  correct2 = int(input('정답[2]: '))

  if correct1 == rn1 and correct2 == rn2 :
    score += 1
    print("정답입니다!")
  elif correct1 == rn2 and correct2 == rn1 :
    score += 1
    print("정답입니다! ♪(^∇^*)")
  else:
    print("오답입니다 (T_T)")
      
  if score == 3:
    print("3점을 달성하였습니다! 게임이 종료됩니다. 🙇‍♂️")
    break
  else:
    print("좀 더 노력해보세요! 🙋‍♂️")
    print("")
    continue
