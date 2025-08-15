x=0
y=1
while True:
    g=x+y
    x=y
    y=g
    if g >=100:
        break
    print(g)