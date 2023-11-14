word = input(" Enter a sentense and symbol: ")
sym = input(" Enter a sym: ")
pose = word.find(sym)
if pose != -1:
    print (" Sym: " , sym  , pose)
else:
    print("There is no sym: " , sym)
