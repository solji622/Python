c = input("기침이 있나요: ")
f = float(input("체온: "))
if c == 'Y' and f >= 38.5:
    print("독감일 수 있습니다")
else :
  print("독감이 아닙니다")
