a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b:
    if a > c:
        if a > d:
            print(a)
        else:
            print(b)
    else:
         if c > d:
             print(c)
         else:
             print(d)
else:
  if b > c:
      if b > d:
          print(b)
      else:
          print(d)
  else:
         if c > d:
             print(c)
         else: 
             print(d)

