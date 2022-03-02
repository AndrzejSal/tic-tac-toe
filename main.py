
x = ["-","-","-"]
y = ["-","-","-"]
z = ["-","-","-"]

def plansza():
    #print('\n','\n','\n','\n','\n','\n','\n','\n')
#    #os.system("clear")
    print('\n',*x,'\n',*y,'\n',*z,sep=" ") #,end="").
def ustaw(co,gdzie):
    gdzie -= 1
    if gdzie > 5:
        gdzie-= 6
        x[gdzie] = co
    elif gdzie > 2:
        gdzie -=3
        y[gdzie] = co
    else:
        z[gdzie] = co
        #print(z)
plansza()

def przeczytaj(gdzie):
    global x,y,z
    g = {1:z,2:z,3:z,4:y,5:y,6:y,7:x,8:x,9:x,}
    if gdzie < 4:
        return (g[int(gdzie)])[int(gdzie-1)]
    elif gdzie < 7:
        return (g[int(gdzie)])[int(gdzie-4)]
    elif gdzie < 10:
        return (g[int(gdzie)])[int(gdzie-7)]
    else:
        return ("Błąd adresu")













#.