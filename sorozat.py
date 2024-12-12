import random



def dobas():
    import random
print("II/A,B,C:")

import random


erme= ["Fej", "Írás"]
logikai_kimenetek = [1, 0]  


dobasok = []
logikai_dobasok = []


for i in range(7):
    
    eredmeny = random.random()
    if eredmeny < 0.5:
        dobasok.append("Fej")
        logikai_dobasok.append(1)
    else:
        dobasok.append("Írás")
        logikai_dobasok.append(0)


for i in range(len(dobasok)):
    if i == len(dobasok) - 1:
        print(dobasok[i])  
    else:
        print(dobasok[i], end="-")




