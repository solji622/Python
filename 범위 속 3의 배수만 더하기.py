sum = 0
while True:
  for i in range(1, 1001, 1):
    if i % 3 == 0:
      sum += i
  break
print(sum)
