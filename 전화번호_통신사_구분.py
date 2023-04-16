num = input("휴대전화 번호 입력: ")
if "011-" in num : #num 안에 011- 이 있다면
  print("당신은 SKT 사용자 입니다")
elif "016-" in num : #num 안에 016- 이 있다면
  print("당신은 KT 사용자 입니다")
elif "019-" in num : #num 안에 019- 이 있다면
  print("당신은 LGU 사용자 입니다")
elif "010-" in num : #num 안에 010- 이 있다면
  print("당신은 알수없음 입니다")
