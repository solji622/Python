# 가위 = 1 바위 = 2 보 = 3


A = int(input("가위바위보: "));
B = int(input("가위바위보: "));

if B > A : #B가 A보다 크다면
  print("B가 이겼다!")
elif A == 3 and B == 1: #A가 3이고 B가 1이면
  print("B가 이겼다!")
elif B < A : #B가 A보다 작으면
  print("A가 이겼다!")
elif A == B : #A와 B가 같다
  print("비겼다!")
