a = 12
b = 5
c = a
d = b
while True:
 rem = c%d
 if rem==0:
  print("HCF:",d)
  lcm = (a*b)/d
  print("LCM:",lcm)
  break
 else:
  c = d
  d = rem

