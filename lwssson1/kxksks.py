py = int(input("Enter your level of python(99): "))
db = int(input("Enter your level of Database(99): "))
dj = int(input("Enter your level of Django(99): "))

if  500 and 1000 and 1200:

  rating = (py * 5) + (db * 4) + (dj * 3)
  if rating >= 1000 and 1200 >= 1000:
      message = "You are accepted!"
  elif rating <= 1000 or 500 < 1000:
      message = "We are gonna contact you."
  else:
      message = "You are not accepted."
 
  print(f"Rating : {rating}")
  print(message)
else:
      print("You entered wrong indications(0-100)")