# bounce.py
# test
# Exercise 1.5
height = 100
dropDecrease = 3/5
bounceMax = 10
bounceCount = 1

while bounceCount <= bounceMax:
    print(bounceCount, round(height*dropDecrease,4))
    height = height*dropDecrease
    bounceCount = bounceCount + 1

