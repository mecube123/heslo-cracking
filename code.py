heslo = input("zadejte heslo od 1 do 6 znaků: ")
#udělá proměnnou heslo pomocí které budeme pracovat
znaky = ["q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Y", "X", "C", "V", "B", "N", "M", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ":", "?", "<", ">", "_", "Ů", "ů", "$", " ", "!", "ß", "§", "'", "¤", "/", "(", ")", "×", "*", "-", "+", "#"]
#seznam se všema znakama z abecedy (vypište všechno i malá i velká písmena)
znaky1 = znaky
znaky2 = znaky
znaky3 = znaky
znaky4 = znaky
znaky5 = znaky
#proměnné pomocí kterých budeme pracovat aby nám vypsali čísla
len_heslo = len(heslo)
#počet znaků na tom, co jste zadali hned na poprvé (řadek 1)
if len_heslo > 6:
    print("heslo má víc jak 6 znaků!!!")
    exit()
#když má heslo víc jak 6 znaků, tak vám vypíše že to má víc a ukončí program
if len_heslo == 0:
    print("tvoje heslo nemá znaky")
#když heslo nemá žádné znaky tak to vypíše že to nemá znaky 
if len_heslo == 1:
    for i in znaky:
        print(i)
        if i == heslo:
            exit()

if len_heslo == 2:
    for i in znaky:
        for x in znaky1:
            q = i+x
            print(i+x)
            if q == heslo:
                exit()
if len_heslo == 3:
    for i in znaky:
        for x in znaky1:
            for y in znaky2:
                q = i+x+y
                print(i+x+y)
                if q == heslo:
                    exit()
if len_heslo == 4:
    for i in znaky:
        for x in znaky1:
            for y in znaky2:
                for z in znaky3:
                    q = i+x+y+z
                    print(i+x+y+z)
                    if q == heslo:
                        exit()
if len_heslo == 5:
    for i in znaky:
        for x in znaky1:
            for y in znaky2:
                for z in znaky3:
                    for t in znaky4:
                        q = i+x+y+z+t
                        print(i+x+y+z+t)
                        if q == heslo:
                            exit()
if len_heslo == 6:
    for i in znaky:
        for x in znaky1:
            for y in znaky2:
                for z in znaky3:
                    for t in znaky4:
                        for u in znaky5:
                            q = i+x+y+z+u
                            #tady se vytvoří proměnná q, kterou budeme pouažívat na řádku 69
                            print(i+x+y+z+u)
                            if q == heslo:
                                exit()
                                #tady se píše že když se q rovná heslo tak má ukončit program (zastavit na čísle který jste tam zadala)
#tady jsou už jenom cykly v cyklu protože čím víc znaků tím víc cyklů
