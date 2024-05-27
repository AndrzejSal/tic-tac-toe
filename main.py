
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
    g = [z,y,x][(gdzie-1)//3]
    return g[(gdzie-1)%3]
    #else:
    #    return ("Błąd adresu")













#.
