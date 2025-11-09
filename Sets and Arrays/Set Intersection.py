setx = {"ria", "tina"}
sety = {"mina", "ele"}
print("Original set elements:")
print(setx)
print(sety)
print("/nIntersection of two said sets:")
setz = sety.intersection(setx)
print(setz)
seta=setx.union(sety)
print(seta)

setb=setx.difference(sety)
print(setb)