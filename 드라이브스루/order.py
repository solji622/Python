import random
guest = []

for i in range(1,4,1):
  #손님을 임의로 세명 받음
  guest.append(i)
  print(i,"번째 손님이 들어왔습니다")

print()
print("어서오세요 *입니다")
print()

#음식 제조
def cook():
  if order == 1 :
    print("1번 메뉴 햄버거 단품 주문 들어왔습니다")
    print(hamburger_bun.pop(),"번째 번 올리기")
    print(hamburger_patty.pop(),"번째 패티 올리기")
    print(cheese.pop(),"번째 치즈 올리기")
    print("마지막으로 ",hamburger_bun.pop(),"번째 번 올리기")
    print("햄버거 완성 🍔")

  elif order == 2 :
    print("2번 메뉴 콜라(R) 주문 들어왔습니다")
    print("컵에 콜라 채우는 중···")
    print("███▒▒")
    print("█████▒")
    print("███████")
    print("콜라 완성 🥤")

  elif order == 3 :
    print("3번 메뉴 들어왔습니다")



#손님 주문
for i in guest:
  #랜덤 객체를 이용하여 손님의 주문을 랜덤으로 받음
  order = random.randrange(1,4,1)
  print("손님이",order,"번 메뉴를 주문하였습니다")
  print()
  cook()
  print()
  print("주문하신 음식이 나왔습니다")

  #손님 퇴장 - 큐 이용
  print(guest.pop(0),"번째 손님이 나갔습니다")
  print()

  #손님 없을 경우
  if len(guest)==0:
    print("손님이 없습니다")


#요리 재료 리스트로 쌓기 (제조 시 스텍으로 빼냄)
hamburger_bun = [1,2,3,4]
hamburger_patty = [1,2]
cheese = [1,2]
