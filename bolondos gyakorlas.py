while True:
    try:
        hany_diak = int(input("hány diákot szeretne hozzáadni "))
        if type(hany_diak) == int:
            break
    except:
        print("rossz input")
        
    diakok = []    
        
for i in range(hany_diak):
    nev = input("add meg a diák nevét")
    try:
        
        jegy = int(input("add meg a diák jegyét"))
    except:
        print("rossz input")
   
osszes_diak = input("szeretné látni az összes diákot?")

    

    
   