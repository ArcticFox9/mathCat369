import time
import random
#math_gods.py
print ("HIYYYYYYYY")
print("THIS IS A PROGRAM TO MAKE UUUU A MATH GOD \n I HAD 14 CUPS OF COFFE THIS MORNING")
print("YOOOOOOR NAME IZZZZ CHEZZZZZZZZ HEADDDD \n HELLLLLLLOZZZZZZ CHEZZZZZZZZ HEADDDD")



for i in range(0,5):
    print ("problem",i)

    x = random.randrange(1,12)
    #print("x is",x)
    y = random.randrange(1,12)
    #print("y is",y)

    print(x, " X ", y , "=")
    time.sleep(7)
    print(x, " X ", y , "=" , (x*y))
