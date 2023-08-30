import random
guest = []
mistake = 0

#손님 수를 랜덤으로 받음
guestrn = random.randrange(1,11,1)
for i in range(1,guestrn+1,1):
  guest.append(i)

print("손님이",guestrn,"명 들어왔습니다")
print()
print("-"*40)
print("어서오세요 원숭이와 아이들🐵 입니다")
print("-"*40)


#1번 메뉴 요리 재료 리스트로 쌓기 (제조 시 스택으로 빼냄)
hamburger_bun = [1,2,3,4,5,6]
hamburger_patty = [1,2,3,4]
cheese = [1,2,3]

#음식 제조
def cook():
  if a == 1 :
    #재료가 부족할 경우 새로 추가
    if len(hamburger_bun) == 0:
      hamburger_bun.append(1)
      hamburger_bun.append(2)
    if len(hamburger_patty) == 0:
      hamburger_patty.append(1)
      hamburger_patty.append(2)
    if len(cheese) == 0:
      cheese.append(1)
      cheese.append(2)
    print(hamburger_bun.pop(),"번째 번 올리기")
    print(hamburger_patty.pop(),"번째 패티 올리기")
    print(cheese.pop(),"번째 치즈 올리기")
    print("마지막으로 ",hamburger_bun.pop(),"번째 번 올리기")
    print("햄버거 완성 🍔")

  elif a == 2 :
    print("컵에 콜라 채우는 중···")
    print("███▒▒")
    print("█████▒")
    print("███████")
    print("콜라 완성 🥤")

  elif a == 3 :
    print("바나나 껍질 벗기기")
    print("바나나 완성🍌")

  else:
    print("없는 메뉴입니다")


#손님 주문
for i in range(1,guestrn+1,1):
  #랜덤 객체를 이용하여 손님의 주문을 랜덤으로 받음
  order = random.randrange(1,4,1)
  print()
  print(guest[0],"번째 손님이",order,"번 메뉴를 주문하였습니다")
  print()

  #계산원이 주방장에게 신호보내기
  a = int(input("[🙆‍♂️] 1.햄버거 단품 / 2.콜라 / 3 ❔ : "))
  print("[👨‍🍳] ",a,"번 메뉴 제조 시작합니다")
  print()

  #주문 들어온 것과 요청이 맞지 않는 경우
  if order != a :
    print("맞지 않는 요청입니다. 다시 주문해주세요")

    #직원 실수 누적시키기
    mistake += 1
    print("[👾] system: 실수",mistake,"번 누적되었습니다.")
    print("-"*40)
    continue



  #음식 제조 (cook 함수 사용)
  cook()
  print("-"*40)

  if a == 1:
    print("주문하신 🍔햄버거 단품이 나왔습니다")
  elif a == 2:
    print("주문하신 🥤콜라 나왔습니다")  
  elif a == 3: 
    print("주문하신 ★스페셜★ 🍌최영원의 바나나 나왔습니다") 
  print("-"*40)

  #손님 퇴장 - 큐 이용
  print(guest.pop(0),'\033[1m' + "번째 손님이 나갔습니다"+ '\033[0m')
  print("-"*40)

  #손님 없을 경우
  if len(guest)==0:
    print("손님이 없습니다")
  
  #실수 3회 이상 누적 시 해고
  if mistake >= 3:
      print()
      print("[👾] system: 실수 3회 이상 누적으로 당신은 해고되었습니다.")
      break
