two_dice = range(1,6)
kuu = [[x,y,z] for x in two_dice for y in two_dice for z in two_dice]
for a in kuu:
    if sum(a) == 5:
        print(a)

