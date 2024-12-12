def jatekos():
    print("I/A:")
    jatekosneve:str = str(input("Játékos neve: "))
    szerepkor:str = str(input("szerepkör:\n"))
    print("I/B:")
    if (szerepkor == "varázsló"):
        print(f"Üdvözlünk {jatekosneve}, 2 életed van!")
    elif (szerepkor == "harcos"):
        print(f"Üdvözlünk {jatekosneve}, 10 életed van!")
    else:
        print(f"Üdvözlünk {jatekosneve}, 8 életed van!")