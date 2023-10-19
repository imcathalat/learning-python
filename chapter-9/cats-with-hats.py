cats_list = [False] * 100 


cats_with_hats = []
cats_list = [True] * (100 + 1)
for round in range(2, 100 + 1):

    if round % 2 == 0:
        for cat in range(0, 100):
            if cat % 2 == 0:
                if cats_list[cat] is True:
                    cats_list[cat] = False
                else: 
                    cats_list[cat] = True
    else:
        for cat in range(0, 100):
            if cat % 2 != 0:
                if cats_list[cat] is True:
                    cats_list[cat] = False
                else: 
                    cats_list[cat] = True
    
    for cat in range(0, 100):
        if cats_list[cat] is True:
            cats_with_hats.append(cat)



print(cats_with_hats)

