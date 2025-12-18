
def do_stuff(x, y):
    temp = x + y
    if temp > 10:
        if temp < 100:
            if temp != 50:
                print("it is ok")
            else:
                print("middle")
        else:
            print("too big")
    else:
        print("too small")

    return temp

a = 1
b = 2
c = do_stuff(a, b)
print(c)
