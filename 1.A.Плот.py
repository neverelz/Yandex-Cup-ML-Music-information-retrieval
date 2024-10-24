WSx = int(input())
WSy = int(input())
NEx = int(input())
NEy = int(input())
tx = int(input())
ty = int(input())

if ty > NEy:
    print("N", end='')
elif ty < WSy:
    print("S", end='')
if tx > NEx:
    print("E")
elif tx < WSx:
    print("W")
