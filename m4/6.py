name = ['Arm','Bobby','Cathy','Dorothy','Emily']
score = [86,78,54,65,34]
alls = [[x,y] for x,y in zip(name,score)]
for x,y in alls:
    if y >= 80:
        print(x ,"4")
    elif y >= 70:
        print(x,"3 warning")
    else:
        print(x,"2")
            

