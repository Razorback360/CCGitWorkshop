a, b = 0, 1
n = int(input())
for i in range(n):
  print("-Yippe-" * b)
  a, b = b, a + b
