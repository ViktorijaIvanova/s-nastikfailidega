from Omamoodul import*
rus=[] 
est=[]
while True:
     v=int(input("1-loema failist/n2-translate/n3-tekstist kõne/n"))
     if v==1:
        rus=kirjuta_faili("rus.txt")
        est=kirjuta_faili("est.txt")
        for line in rus,est:
            print(line)
     elif v==2:
       translate
        